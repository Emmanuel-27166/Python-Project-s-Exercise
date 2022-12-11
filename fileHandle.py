
# example of read files 
f = open ("DataOpen", 'r')


print(f.read(), end="")
print(f.readline())

# =================================================================
ab = open("DataOpen", 'r')
print(ab.read(), end="")

# example of write files
writeFile = open("abc", 'w')
writeFile.write("here we write a list of sentences as you would like them")