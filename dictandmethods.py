dict1 = {} # empty dictionary
print(type(dict1))

#Dictionary is a key-value pair type D-S and it is mutable
dict = {"good": "something pleasant", "fetch": "to bring", "1": "The number 1"}

marks = {"Harshit" : 34, "Harry" : 99, "Shivani": 8, "Smriti": 45, "Naina": 87}

print(dict["good"])
print(marks["Harry"])

marks["priya"] = 34
print(marks)

print(marks.get("priyanka")) # this won't show us error returns none
print(marks["priyanka"]) # this will show us error
print(marks.values())
print(marks.keys())
print(marks.items())

