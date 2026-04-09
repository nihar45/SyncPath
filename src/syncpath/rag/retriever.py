"""Transparent lexical retrieval for the local documentation corpus."""
import re
from .corpus import PASSAGES
STOP={'what','when','where','how','does','the','and','for','with','this','that','are','can','you','a','of','is','to','in','on'}

def terms(text):
    return set(t for t in re.findall(r'[a-z0-9]+',text.lower()) if t not in STOP)

def retrieve(question, passages=None, limit=3):
    passages = PASSAGES if passages is None else passages
    tokens=terms(question)
    ranked=[]
    for item in passages:
        score=len(tokens & terms(item.title))*3+len(tokens & terms(item.text))
        if score:ranked.append((score,item))
    ranked.sort(key=lambda pair:(-pair[0],pair[1].id))
    return [item for _,item in ranked[:limit]]
