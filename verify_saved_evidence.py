"""Read-only cross-check of saved v7.13 JSON evidence; NOT a simulation rerun."""
import argparse, collections, json, zipfile, hashlib
from pathlib import Path

def audit(path):
    with zipfile.ZipFile(path) as z:
        names=z.namelist()
        inventory_name=next(n for n in names if 'B01_B24_Six_Arm_Inventory_' in n and n.endswith('.json'))
        inv=json.loads(z.read(inventory_name))
        per={}
        discrepancies=[]
        counts=collections.Counter()
        for i in range(1,25):
            target=f'B{i:02d}'
            matches=[n for n in names if f'{target}_Six_Arm_Profile_Exploratory_' in n and n.endswith('.json')]
            if len(matches)!=1:
                discrepancies.append(f'{target}: expected one evidence JSON, found {len(matches)}');continue
            data=json.loads(z.read(matches[0]))
            statuses={}
            for label,e in data['endpoint_results'].items():
                F=float(e['F']);E=float(e['E']);tau=float(e['tau'])
                if abs(tau-max(1e-8,5*E))>1e-8:
                    discrepancies.append(f'{target}/{label}: tau mismatch')
                if F>tau: status='robust_positive'
                elif F < -tau and e.get('common_negative') is True: status='robust_negative'
                else: status='unresolved_numerical_margin'
                if status!=e['status']:
                    discrepancies.append(f'{target}/{label}: calculated {status}, archived {e["status"]}')
                counts[status]+=1;statuses[label]=status
            per[target]=statuses
            if data.get('bracket_status') != 'unresolved_numerical_margin':
                discrepancies.append(f'{target}: non-unresolved bracket')
        target_map={x['target']:x for x in inv['targets']}
        for target,statuses in per.items():
            if target not in target_map or statuses != target_map[target]['endpoints']:
                discrepancies.append(f'{target}: inventory endpoint mismatch')
        return {'archive_sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),
                'check_type':'Saved JSON cross-check only; no numerical integrations rerun',
                'targets_checked':len(per),'endpoints_checked':sum(counts.values()),
                'recomputed_saved_label_counts':dict(counts),
                'archive_bracket_counts':inv['bracket_status_counts'],
                'archive_physical_hessian_executed_count':inv['hessian_executed_count'],
                'discrepancies':discrepancies,'status':'PASS' if not discrepancies and len(per)==24 else 'INCOMPLETE_OR_FAIL'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('archive');p.add_argument('--out');a=p.parse_args()
    result=audit(a.archive);output=json.dumps(result,indent=2)
    if a.out:Path(a.out).write_text(output+'\n')
    print(output)
