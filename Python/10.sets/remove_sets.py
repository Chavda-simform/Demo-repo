# remove set item uisng remove key woerd 
# If item is not present in array then it will throw an error
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# Discard items in using disacrd item 
# note :- If item is not presint in set then it will not thow error_

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


# remove rendom item form set
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)


# clear method is use for remove all element form set

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


# Del keyword delete hole set
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

