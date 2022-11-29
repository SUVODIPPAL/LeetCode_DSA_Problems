def reverseinteger(num):
    rev=0
    sign=1
    if num<0:
        sign=-1
        num=num*-1
    while num>0:
        a=num%10
        rev=rev*10+a
        num//=10
    if not -(2**31)-1 < rev < 2**31:
        return 0
    return sign*rev

print(reverseinteger(-120))