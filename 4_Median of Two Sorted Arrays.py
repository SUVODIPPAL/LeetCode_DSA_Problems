def twosortedarr(arr1,arr2):
    arr3=[]
    other=0
    sum=0
    mid=0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] not in arr3:
                arr3.append(arr1[i])
            if arr2[j] not in arr3:
                arr3.append(arr2[j])
    arr3.sort()
    length=len(arr3)
    other=length%2

    if other != 0:
        print(float(arr3[length//2]))
        
    else:
        sum=arr3[length//2-1]+(arr3[length//2])
        print(sum/2)

arr1=[3,4]
arr2=[1,2]
print(arr1,arr2)
prt=twosortedarr(arr1,arr2)
print(prt)
