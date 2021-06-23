def withdraw(amount, balance):
       if balance > amount:
              print("Please take your cash of $", amount," from the machine" )
              db_balance = balance - amount
              
       else:
              print("Insufficient fund in your account")


def balance(balance):
       print("You currently have $",balance)


vPin = "3000"
db_balance = 2500000
#reuse = 0

while True:
       #reuse = resuse + 1
       print("****** THIS IS FIDELITY BANK ATM *******")
       print("Please insert your card into the machine")
       pin = input("Enter your 4 digit pin to proceed\n")



       if pin == vPin:
              opt = input("ENTER:\n1. To withdraw\n2. TO check balance\n3. To transfer"
                          + "\n4. To airtime\n")

              
              if opt == "1":
                     #withdraw
                     colAmount = input("ENTER:\n1. $1000\n2. $2000\n3. $5000"
                            +"\n4. $10000\n5. $20000\n6. Others\n")
                     
                     if colAmount == "1":
                            withdraw(1000, db_balance)
                     
                     elif colAmount == "2":
                            withdraw(2000, db_balance)
                            
                     elif colAmount == "3":
                            withdraw(5000, db_balance)
                            
                     elif colAmount == "4":
                            withdraw(10000, db_balance)
                            
                     elif colAmount == "5":
                            withdraw(20000, db_balance)
                            
                     elif colAmount == "6":
                            otherAmount = input("Enter the amount you will like to "
                            + "withdraw in $\n")
                            
                            withdraw(int(otherAmount), db_balance)
                            
                     else:
                            print("Invalid input")
                            
              elif opt == "2":
                     balance(db_balance)
                     
              elif opt == "3":
                     #Transfer
                     
                     print("3")
                     
              elif opt == "4":
                     #airtime
                     print("4")
                     
              else:
                     print("Invalid input")
                     
       else:
              print("Invalid pin")
              print("Please take your ATM")
       
