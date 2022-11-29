# def zigzagConversion(str,row=4):
#     pat=[[] for i in range(row)]
#     k=0
#     for i in range(len(str)):
#         if i%2!=0:
#             pat[1].append(str[i])
#         else:
#             if k%2==0:
#                pat[0].append(str[i])                
#             else:
#                pat[2].append(str[i])
#             k+=1
#     for j in range(len(pat)):
#         if j%2==0:
#             for i in (pat[j]):
#                 print(i,end=" ")
#         else:
#             print("\n")
#             for i in pat[j]:
#                 print(i,end="")
#             print("\n")
#     print()
#     print(pat[0]+pat[1]+pat[2])
# str="suvodippal"
# zigzagConversion(str)





def zigzagConversion(str,row):
    s=""
    for i in range(row):
        increment=2*(row-1)
        for j in range(i,len(str),increment):
            s+=str[j]
            if (i>0 and i<row-1 and j+increment-2*i<len(str)):
                s+=str[j+increment-2*j]
    return s

str="suvodippal"
row=4
new=zigzagConversion(str,row)
print(new)