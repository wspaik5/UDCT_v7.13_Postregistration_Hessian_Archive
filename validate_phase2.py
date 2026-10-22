"""Read-only reproducibility cross-check of archived UDCT v7.13 arrays."""
import sys, zipfile, io, json, hashlib, collections, ast
import numpy as np
from pathlib import Path

def validate(path):
    path=Path(path)
    with zipfile.ZipFile(path) as z:
        names=z.namelist()
        inv=json.loads(z.read(next(n for n in names if 'B01_B24_Six_Arm_Inventory_' in n and n.endswith('.json'))))
        n=next(n for n in names if 'B01_B24_All_Common_Profiles_' in n and n.endswith('.npz'))
        arrays=np.load(io.BytesIO(z.read(n)),allow_pickle=False)
        groups=collections.defaultdict(list)
        for key in arrays.files:
            target,endpoint,grid,cutoff=key.split('|')
            groups[(target,endpoint)].append(np.asarray(arrays[key]))
        results={}
        for (target,endpoint),profiles in sorted(groups.items()):
            stack=np.stack(profiles)
            # E is the max pointwise range across the six arms.
            E=float(np.max(np.max(stack,axis=0)-np.min(stack,axis=0)))
            tau=max(1e-8,5*E)
            minimum=float(np.min(stack))
            common_witness=bool(np.any(np.all(stack < -tau,axis=0)))
            results[f'{target}|{endpoint}']={'arms':len(profiles),'samples':int(stack.shape[1]),'E_common':E,'tau_common':tau,'minimum_common':minimum,'common_negative_witness':common_witness}
        dup=[x for x in names if 'B19_Six_Arm_Profile_Exploratory_' in x and x.endswith('.json')]
        b18=[x for x in names if 'B18_Six_Arm_Profile_Exploratory_' in x and x.endswith('.json')]
        py=[x for x in names if x.endswith('.py')]
        syntax=[]
        for p in py:
            try: ast.parse(z.read(p).decode('utf-8-sig'),filename=p)
            except Exception as exc: syntax.append({'file':p,'error':str(exc)})
        b01={k:v for k,v in results.items() if k.startswith('B01|')}
        b18r={k:v for k,v in results.items() if k.startswith('B18|')}
        return {'method':'archived-array analysis, not independent integration','archive_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'python_scripts':len(py),'python_syntax_failures':syntax,'endpoint_groups':len(groups),'common_profiles':len(arrays.files),'all_groups_six_arms':all(v['arms']==6 for v in results.values()),'all_profiles_1200_samples':all(v['samples']==1200 for v in results.values()),'common_negative_witness_groups':[k for k,v in results.items() if v['common_negative_witness']],'B01':b01,'B18':b18r,'B18_target_JSON_count':len(b18),'B19_target_JSON_count':len(dup),'B19_duplicate_byte_identical':len(dup)==2 and z.read(dup[0])==z.read(dup[1]),'inventory_B18':next(x for x in inv['targets'] if x['target']=='B18'),'limitations':['Common-domain NPZ cannot reconstruct native-grid F minima','Cannot claim independent simulation or full physical 3D Hessian','Archived inventory labels are not independently validated from native minima']}
if __name__=='__main__':
    result=validate(sys.argv[1]);print(json.dumps(result,indent=2))
