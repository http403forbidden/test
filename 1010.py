import copy
list1 = [1,2,3]
#c = list1
#print(id(list1))
#print(id(c))

a = copy.copy(list1)
#a = list1
print(id(list1))
print(id(a))
print(id(list1[1]))
print(id(a[1]))


