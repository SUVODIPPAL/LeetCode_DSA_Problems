def longestpalindromsubsstr(str):                       #"paapl"

    max_len=0
    # res=[0,1]
    for i in range(len(str)):
        for j in (0,1):
            left=i
            right=i+j
            while left>=0 and right<len(str) and str[left]==str[right]:
                left-=1
                right+=1
            cur_len=right-left-1
            if cur_len>max_len:
                max_len=cur_len
                res=[left+1,right]
    return str[res[0]: res[1]]            

s="paapl"
print(s)
new=longestpalindromsubsstr(s)
print(new)