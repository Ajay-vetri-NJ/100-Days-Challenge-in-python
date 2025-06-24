from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    
    for s in strs:
        sorted_s = ''.join(sorted(s))
        anagrams[sorted_s].append(s)
    
    return list(anagrams.values())

strs = input("Enter the list of strings separated by spaces: ").split()

grouped_anagrams = group_anagrams(strs)
print(f"The grouped anagrams are: {grouped_anagrams}")
