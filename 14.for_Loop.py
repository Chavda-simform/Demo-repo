# simple for loop for print and items form list

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# continu satement in forloop
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


#  ramge key word is use for spacify range bitwen two values 
for x in range(2, 6):
  print(x)

# nested for loop 
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.