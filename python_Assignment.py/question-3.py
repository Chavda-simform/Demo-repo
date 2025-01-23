

# -----------------------------not complit ----------------------------------------------------------------
# ***********************************************************************************************************

# input = ["eat","tea","tan","ate","nat","bat"]
# in2 = []
# result = []
# for i in input:
#     sh = ''.join(sorted(i))
#     in2.append(sh)
# ic = 0

# for i in in2:
#     for j in in2:

#         if(i == j):
#             # print(input[ic])
#             if input[ic] not in in2:
#                 print(input[ic])
#                 # in2.append(input[ic])
#             # jc +=1
#     # result.append(in2)
#     ic += 1 

# # print(result)


# --------------------------------------Most Optimal Solution-------------------------------------------------
#  ************************************************************************************************************
# # method :- 1

# give input
input = ["eat","tea","tan","ate","nat","bat"]
# input = ["a"]
# input = [""]

# create empty dicsnary
dic = {}


for i in input:
    # shorting the elemnt one by one
    short = ''.join(sorted(i))
    # if elemnt si in dic then append elemnt
    if short in dic:
        dic[short].append(i)
    # else creating a new dic key 
    else:
        dic[short] = [i]

print(dic.values())