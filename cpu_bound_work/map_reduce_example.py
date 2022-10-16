from functools import reduce
from typing import Dict


def map_frequency(text: str) -> Dict[str, int]:
    words = text.split(' ')
    freq = {}
    for w in words:
        if w in freq:
            freq[w]+=1
        else:
            freq[w]=1
    return freq

def merge_dicts(first: Dict[str,int],
                second: Dict[str,int]) -> Dict[str,int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key]+=second[key]
        else:
            merged[key] = second[key]
    return merged

lines = ["i knew what i know",
         "i knew what i don't know",
         "i knew what i know much",
         "i knew what i don't know much"]

mapped_results = [map_frequency(line) for line in lines]

for result in mapped_results:
    print(result)

print(f"fin= {reduce(merge_dicts,mapped_results)}")