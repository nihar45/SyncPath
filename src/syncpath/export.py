"""Write reports to a chosen destination without implicit file mutations."""
import csv,json
from pathlib import Path

def write_json(rows,path):
    target=Path(path)
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')

def write_csv(rows,path):
    target=Path(path)
    target.parent.mkdir(parents=True,exist_ok=True)
    with target.open('w',newline='',encoding='utf-8') as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)
