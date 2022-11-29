# def string_to_integer(st):
#     s=""
#     for i in st:
#         if ord(i)-ord("1")<=9:
#             s+=str(i)
#     print(s)
#     print(type(s))

# string_to_integer("123432 pal fyt65689")

def myAtoi(s: str):
    sign=+1
    res=""
    i=0
    length=len(s)
    while i<length and s[i]==" ":
            i+=1
    if i<length and s[i] in ("+","-"):
        if s[i]=="+":
            sign=+1
        else:
            sign=-1
        i+=1
    while i<length and s[i].isdigit():
            res+=s[i]
            i+=1
    return max(-2**31, min(sign * int(res or 0), 2**31 - 1))

s = "1234suvodip678"
print(myAtoi(s))
