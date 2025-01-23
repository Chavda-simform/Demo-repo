# 2. Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#     Constraints:

#         - 1 <= n <= 8

#     Example 1:

#         - Input: n = 3

#         - Output: ["((()))","(()())","(())()","()(())","()()()"]

#         - Example 2:

#     Example 2:

#         - Input: n = 1

#         - Output: ["()"] 
# ***************************************************************************************************************

# def permutation(word):
#     if len(word) == 1:
#         return [word]

#     perms = permutation(word[1:])
#     char = word[0]
#     result = []

#     for perm in perms:
#         for i in range(len(perm)+1):
#             result.append(perm[:i] + char  + perm[i:])

#     return result   

# print(permutation('abc'))


# *************************************************************************************************************

# method :- 2

# input = int(input("Enter value:- "))
# corv = ['(',')']
# result = []
# ilen = input * 2


# def recursun(ilen,seq = ""):
    
#     # print(input)
#     print(ilen)
#     if ilen == 0:
#         if seq[0] == '(' and seq[-1] == ')' and seq.count('(') == input :
#             return result.append(seq)
#         else: 
#             return 
#     for i in corv:
#         # ilen = ilen -1
#         recursun(ilen - 1, seq + i)
        
# recursun(ilen)
# print(result)

#-------------------------------------------- Most Optimal Aproch -----------------------------
# ************************************************************************************************************

# method :-3
# Enter Inut form User
input = int(input("enter input"))
# set Global variable
oc = 0
cc = 0
result = []
# create function for setting of parenthesis 
def rec (oc,cc,s = ""):
    # chanking value opning and closing is not out of bound 
    if(oc == input and cc == input):
        result.append(s)
    # chacking opening is less then input number
    if(oc < input):
        rec(oc+1,cc,s+'(')
    # chacking closing is less then opening parenthesis 
    if(cc < oc):
        rec(oc,cc+1,s+')')
# Calling function 
rec(oc,cc)
# printing result
print(result)