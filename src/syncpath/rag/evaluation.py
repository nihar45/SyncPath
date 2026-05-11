"""Small labeled relevance set for documentation retrieval."""
from .retriever import retrieve

QUERIES={
    'idempotency key repeat write':'NET-003',
    'network handoffs cellular wifi':'NET-005',
    'offline queue connectivity':'NET-001',
    'acknowledgment timeouts server effects':'NET-004',
    'retry backoff transient failures':'NET-002',
}

def evaluate_top1():
    rows=[(query,expected,(retrieve(query,limit=1)[0].id if retrieve(query,limit=1) else None)) for query,expected in QUERIES.items()]
    return {'correct':sum(expected==actual for _,expected,actual in rows),'total':len(rows),'cases':rows}
