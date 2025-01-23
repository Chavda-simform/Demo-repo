# 1. Write a program for computing GCD of 2 numbers with optimal data structures and less time-consuming.

#     The program should take input from console or args and should handle unexpected inputs    

#     Constraints:

#         - For loop is not allowed

#         - input should be in words:

#             - e.g.: onetwo = 12, sixone = 61

#         - words will be within zero to nine

#         - Cannot use inbuilt methods like max, min, or any math function    

#     Example 1:

#         - Input 1: onezero

#         - Input 2: twozero

#         - Output: onezero

#     Example 2:

#         - Input 1: twosix

#         - Input 2: twofour

#         - Output: two



# Import Librarys
import sys

# Create carector dicsnarie
word_to_digit = {
    "zero": "0", "one": "1", "two": "2", "three": "3",
    "four": "4", "five": "5", "six": "6", "seven": "7",
    "eight": "8", "nine": "9"
}
# Create global variable
a =0
b =3
fnum = ''

# Create function for convert word in to numbers
def rec(val):
    global a
    global b

    lenval = len(val)
    # slicing the word to find carecter
    v = val[a:b]
    if v in word_to_digit:
        num = word_to_digit[v]
        global fnum 
        fnum = fnum + num
        # Chacking lengh of the varible is out of bound or not
        if(b < lenval):
            a = b
            # if the vlue is not found then takeing next carecter and chack agin in the dicsnary throw recursion 
            b = b + 1
            return rec(val)
        f = fnum
        fnum = ''
        a = 0
        b = 3
        return int(f)
    # if value is not exist then run else code
    else:
        if(b < lenval):
            b = b+1
            return rec(val)
        else:
            # raise Exception('!Please Enter Valid Input')
            sys.exit('!Please Enter Valid Input')
    
# create a function for finding gcd
def gcd(a,b):
    if (b == 0):
        return int(a)
    else:
        return gcd(b, a%b)

# taking First input from user
val = input("Enter First Input :- ").replace(" " , "")
v = val.lower()
num = rec(v)
print("number one is " , num)

# taking second input form user
val2 = input("Enter Second Input :- ").replace(" " , "")
v2 = (val2.lower())
num2 = rec(v2)

print("number two is ",num2)

# If the first vlue is smoler then second value then it detect and swap autometecaly 
if (num < num2):
    temp = num
    num = num2
    num2 = temp
# calling function and get output 
valgcd = gcd(num,num2)


# Printing final output
print("Final value is ", valgcd)
