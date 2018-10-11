import wikipedia
import os,re
def find(query):
    summary=wikipedia.summary(query,sentences=2)
    summary=re.sub(r'\([^)]*\)', '', summary)
    return summary
