l1 = [3,5,234,234,"Harry"]
print(type(l1))
print(l1)
l1.remove("Harry")
print(l1.count(234))
l1.sort()
print(l1)
l1.pop() # will remove last element
print(l1)
l1.append(78)
print(l1)
# l1.clear() # clears whole list
# print(l1) # empty list
l1.extend([89,73,34,2])
print(l1)
print(l1.index(3))
#slicing of list
print(l1[0:4])






