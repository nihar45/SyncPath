"""Human-readable and machine-readable result reports."""
import json

def render_table(rows):
    keys=['strategy','operations','acknowledged','completion_pct','attempts','duplicate_effects']
    widths={key:max(len(key),*(len(str(row[key])) for row in rows)) for key in keys}
    header='  '.join(key.ljust(widths[key]) for key in keys)
    return '\n'.join([header,'-'*len(header)]+['  '.join(str(row[key]).ljust(widths[key]) for key in keys) for row in rows])

def render_json(rows):
    return json.dumps(rows, indent=2)
