__all__ = (
    'groupper',
)

from csv import DictReader
from collections import deque

def group(file):
    groupped_by_email = {}
    chunks = []
    data = DictReader(file, delimiter=',')
    for row in data:
        groupped_by_email.setdefault(row['email'].split('@')[-1], deque()).append(row)
    
    chunk_count = max(map(lambda x: len(x), groupped_by_email.values()))
    keys = list(groupped_by_email.keys())

    for i in range(chunk_count):
        new_chunk = []
        for k in keys:
            try:
                row = groupped_by_email[k].popleft()
                new_chunk.append((row['email'], row['name']))
            except IndexError:
                continue
        chunks.append(tuple(new_chunk))
        

    return tuple(chunks)

