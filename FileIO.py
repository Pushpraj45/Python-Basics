s = "Harry is a good boy"

# Writing a file
# with open("test.txt", "w") as f:
#     f.write(s)
# fp=open("test.txt", "w")
# fp.write(s)
# fp.close()

#reading a file
with open("test.txt", "r") as f:
     s = f.read()
     print(s)