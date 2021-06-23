print("This is a Prime Number Cheacker")
number = input("Please enter a number\n")
number = int(number)
divisor = 2
if number == 1 or number == 2:
       print("Number is a prime number")
else:
       while True:
              if (number % divisor)== 0:
                     print("Number is not a prime number")
                     break
              
                            
              else:
                     if (number/ divisor) > divisor:
                            divisor = divisor + 1
                     else:
                            print("Number is a prime number")
                            break


       
      
              















       
       
                     
