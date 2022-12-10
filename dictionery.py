myDic = {
    "Name" : "emmanuel",
    "age" : 25,
    "address" : "Freetown",
    "college" : "IPAM",
    "friends" : "ib, bakarr, abdul",
}
print(type(myDic))
print(myDic)
print(myDic.get("age"))
# change a value of a dictionery

myDic["age"] = 43

print(myDic.get("age"))

for x in myDic:
    print(x)