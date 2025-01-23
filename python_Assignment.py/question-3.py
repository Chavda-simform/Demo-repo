

# -----------------------------complited but not optimal-----------------------------------------------------
# ***********************************************************************************************************
# Method -2
input = ["eat","tea","tan","ate","nat","bat"]
in2 = []
result = []
for i in input:
    sh = ''.join(sorted(i))
    in2.append(sh)
diic = {}

for i in range(len(in2)):
    v = []
    for j in range(len(in2)):

        if(i == j):
            # print(in2[i] ,in2[j] , input[j])
            if in2[j] in diic :
                    diic[in2[j]].append(input[j])
            else:
                 diic[in2[j]] = [input[j]]

print("result is :-" , list (diic.values()))


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

print(list(dic.values()))