# class myClass:
#    def __init__(self, name, age):
#     self.name = name
#     self.age = age

# myobje = myClass("emmanuel", 9)
# print(myobje.age)
# print(myobje.name)

# class myClass2:
#     def __init__(self, brother, sister):
#        self.sister = sister
#        self.brother = brother
#        print("the name of my brother is " + brother +    " and sister is " + sister)
       
#     def myFuction(self):
#         print("hellllllllllllo all")

# # create an objec for the class
# myobj2 = myClass2( "Moss", "sarah")
# myobj2.myFuction()

      



print("=================================")
print()
















from objeAndClassExercis import *

class Animal:
    # constructor
    def __init__(self, animalName, animalType):
        self.animalName = animalName
        self.animalType = animalType
        print("the name of the animal is " + animalName + "and the type is " + animalType)

    # let us create methods
    def myMethod1(self):
        print("hello let's get started for today's session")

    def myMethod2(self):
        name = "emmanuelw"
        age = 101
        try:
            if(name == "emmanuel"):
                print("your name is " + name)
            elif(name != "emmanuel" & age != 10):
                print("all is false try again ")
        except:
            print("error along the line")


    def myMethod3(self, animalDisc, animalHeight):
        print("the color of the animal is "+ animalDisc +  " \nand the height of the animal is " +animalHeight)
    def myMethod4(self):
        pass

# create an object of the class
myObject = Animal("Dog", "four legged")
myObject.myMethod1()
myObject.myMethod2()
myObject.myMethod3("red","34.0mm")
















print()
print("=========================================")