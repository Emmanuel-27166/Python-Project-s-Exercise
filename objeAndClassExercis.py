print()
print()
class myClass:
    def  myMrkFunc():
        print ("hello! welcome to grade checker ")
        try:
        # declear the input variable
            exam = int(input("what is your Exam grade? : "))
            cA = int(input("what is your CA grade? :  "))
            totalMark = (exam * 0.7) + (cA * 0.3)
# here we pass the conditions for the exam  
      
            if totalMark >= 70:
                print("You got 4.0 [A] Excellent")
            elif totalMark >= 65:
                print("You got 3.75 [B+] Very Good")
            elif totalMark >= 60:
                print("You got 3.25 [B] Good")
            elif totalMark >= 55:
                print("You got 3.00 [B-] Good")
            elif totalMark >=50:
                print("You got 2.75 [C+] Credit")
            elif totalMark >= 45: 
                print("You got 2.25 [C] Credit")
            elif totalMark >=40:
                print("You got 2.00 [C-] Pass")
            elif totalMark >=35:
                print("You got 1.75 [D] Pass")
            elif totalMark >=30:
                print("You got 1.25 [E] Fail")
            else:
                print(" You Fail wonderful Try to resit ")
            
        except:    
            print()
            print("invalid number try again")

        


# create an obje of the class
myExam = myClass()
myClass.myMrkFunc()

