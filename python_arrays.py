x = [0.0, 3.0, 5.0, 2.5, 3.7] #define an array
print(type(x))

#remove the third element
x.pop(2)
print(x)

#add an element at the end
x.append(1.2)
print(x)

#get a copy
y = x.copy()
print(y)

#how may elements are 0.0
print(y.count(0.0))

#print the index with value 3.7
print(y.index(3.7))

#sort the list
y.sort()
print(y)

#reverse sort
y.reverse()
print(y)

#remove all elements
y.clear()
print(y)