nums = [2,7,11,15]
target = 9
sum=0
# dic={}

for i in range(len(nums)):
    sum=target-nums[i]
    for j in range(i+1,len(nums)):
        if nums[j]==sum:
            print(i,j)


# for i,num in enumerate(nums):
#     sum=target-num
#     if sum in dic:
#         print(dic[sum],i)
#     dic[num]=i