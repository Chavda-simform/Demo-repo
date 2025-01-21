# Update tuple vaue using conveting in to list value
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#  add item using adding two tuples in usig + value 

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)