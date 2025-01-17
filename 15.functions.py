# Creating a Function
def my_function():
  print("Hello from a function")

# calling functinos 
def my_function():
  print("Hello from a function")

my_function()

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# Default peramiter in function 

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Return values

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# Posinal value 
def my_function(x, /):
  print(x)

my_function(3)



# key only arguent

def my_function(*, x):
  print(x)

my_function(x = 3)



# Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)