# if try is not run in this case excetption is run 

try:
  print(x)
except:
  print("An exception occurred")


# use for pertikular error
# try:
# print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")



# finally is use every time
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")



# rise is use for generating custom exseption 
  x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")