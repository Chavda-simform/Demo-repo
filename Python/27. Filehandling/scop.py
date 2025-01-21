# local scop
def myfunc():
  x = 300
  print(x)

myfunc()


# Global scop
x = 300

def myfunc():
  print(x)

myfunc()

print(x)


# Global Key word

def myfunc():
  global x
  x = 300

myfunc()

print(x)