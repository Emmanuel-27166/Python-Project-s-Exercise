myList = [12,34,35,56,78,99,'hello',"emma"]
print(type(myList))
print(myList)
print(myList[4])
print(myList[:4])


# loop through a list
for x in myList:
    print(x)

# check if file exits
if 13 in myList:
    print(12)
else:
    print("no")

# length of a list
print(len(myList))

# append a value in list

myList.append("sorie")
print(myList)

# pop 
myList.remove('sorie')
print(myList)
myList.pop()
print(myList)





# f = open('function.py', "r")
# print(f.read())