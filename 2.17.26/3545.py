#https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/description/



s = "adx"
k = 1
ht = {}

for i in s:
    if i in ht:
        ht[i] +=1
    else:
        ht[i] = 1
if len(ht) > k:
    sortedValues = sorted(ht.values())
    print(sum(sortedValues[:len(ht) - k]))
else:
    print(0)