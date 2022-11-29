def PalindromeNumber(n):
    num=n
    number=0
    while num>0:
        add=num%10
        number=number*10+add
        num=num//10
    # print(number)
    if n==number:
        print("True")
    else:
        print("False")
    
n=12345432
PalindromeNumber(n)