#  array is use for storing mutiple value using single name
cars = ["Ford", "Volvo", "BMW"]

#  we can create array using List,tuple and set;

# len is use for gatting lenth of array  
x = len(cars)


# gatting array using loops
for x in cars:
  print(x)

# adding array elemnt using append key woerd
cars.append("Honda")

# pop is use for remove elemnt form array
cars.pop(1)

# remover is use for removing by its name

cars.remove("Volvo")


# Method in array

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list