
def Addition(num1,num2):
       total = num1 + num2
       print("The Addition of ",num1 , " + " , num2 ," is: ", total)

def Subracttion(num1,num2):
       total = num1 - num2
       print("The Subracttion of ",num1 ," - ", num2 ," is: ", total)

def Division(num1,num2):
       total = num1 / num2
       print("The Division of ",num1 ," / ", num2 ," is: ", total)

def Multiplication(num1,num2):
       total = num1 * num2
       print("The Multiplication of ",num1 ," * ", num2 ," is: ", total)


       
print("******This is a calculator*******")
print("This program solve some basic calculation problems")
firstNum = input("Enter the first number\n")
firstNum = int(firstNum)
opt = input("To perform:\nAddition press 1\nSubtraction press 2\nDivision press 3"
      +"\nMultiplication press 4\n")
secondNum = input("Enter the second number\n")
secondNum = int(secondNum)

if opt == "1":
       Addition(firstNum, secondNum)
       
elif opt == "2":
       Subracttion(firstNum, secondNum)
       
elif opt == "3":
       Division(firstNum, secondNum)
       
elif opt == "4":
       Multiplication(firstNum, secondNum)
       
else:
       print("Oops, wrong input!")



