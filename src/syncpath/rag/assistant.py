"""Answers grounded in retrieved passages without unsupported generation."""
from .retriever import retrieve

def answer(question, limit=3):
    evidence=retrieve(question,limit=limit)
    if not evidence:
        return 'I could not find relevant guidance in the available SyncPath documentation.'
    lines=['Relevant guidance from SyncPath documentation:']
    for item in evidence:
        lines.append(f'- {item.text} [{item.id}] ({item.source})')
    return '\n'.join(lines)
