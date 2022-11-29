def longeststr(s):
    char=set()
    l=0
    res=0
    for i in range (len(s)):
        while s[i] in char:
            char.remove(s[l])
            l+=1
        char.add(s[i])
        res=max(res,i-l+1)
    return res

s="abcdace"
print(s)
new=longeststr(s)
print(new)