reuse = 0
maximum = 3
counter = 0
balance = {'ClientA':500000, 'Brit':600000, 'Ify':800000}
withdrawagain = 3
withdrawcounter = 0
vpin = {'ClientA':"3000",'Brit':"2000",'Ify':"3200"}
print("*******THIS IS A FIDELITY BANK ATM*******")
print("please insert your card")
while counter < maximum:
    name = input("enter your name to proceed\n")
    pin = input("enter your pin to proceed\n")
    try:
        if pin == vpin[name]:
            opt = input("WHAT OPERATION WOULD YOU LIKE TO PERFORM TODAY SIR/MADAM:\n1. Withdrawal\n2. Check balance\n3. Transfer"
                          + "\n4. Buy Airtime\n5. Open a new account")
            break
        else:
            counter+=1
            print('incorrect password\n')
            print('you have ',maximum - counter,'tries left\n')
        #else:
            #print ('TOO MANY TRIES COLLECT YOUR CARD')
            #input()
    except:
        print("Incorrect Input in either name or pin")
    
 #withdraw
if opt== '1':  
         print("HOW MUCH DO YOU WANT TO WITH")
         y=(input("ENTER:\n1. $1,000   2. $2,000\n3. $5,000"
                       + "   4. $10,000\n5. $15,000  6. $20,000\n7. OTHERS\n"))
         if y == "1": 
                print('you have withdrawn $1,000 you have$',balance[name] - 1000,'\nHAVE A NICE DAY')       
         elif y == "2":
                print('you have withdrawn $2,000 you have$',balance[name] - 2000,'\nHAVE A NICE DAY')        
         elif y == "3":
            print('you have withdrawn $5,000 you have$',balance[name] - 5000,'\nHAVE A NICE DAY')
         elif y == "4":
            print('you have withdrawn $10,000 you have$',balance[name] - 10000,'\nHAVE A NICE DAY')
         elif y == "5":
            print('you have withdrawn $15,000 you have$',balance[name] - 15000,'\nHAVE A NICE DAY')
         elif y == "6":
            print('you have withdrawn $20,000 you have$',balance[name] - 20000,'\nHAVE A NICE DAY')
         elif y == "7":
            a=int(input('PLEASE INPUT HOW MUCH YOU WOULD LIKE TO WITHDRAW\n'))
            if a <= balance:
                  print ('YOU HAVE WITHDRAWN',a,'you have $',balance-a,'left \nHAVE A NICE DAY' )
            elif a >=balance:
                         print('AMMOUNT TOO HIGH')
while withdrawagain > 5:
        withdrawagain = withdrawagain + 1
         #withdraw
if opt== '1':  
         print("HOW MUCH DO YOU WANT TO WITH")
         y=(input("ENTER:\n1. $1,000   2. $2,000\n3. $5,000"
                       + "   4. $10,000\n5. $15,000  6. $20,000\n7. OTHERS\n"))
         if y == "1": 
                print('you have withdrawn $1,000 you have$',balance - 1000,'\nHAVE A NICE DAY')       
         elif y == "2":
                print('you have withdrawn $2,000 you have$',balance - 2000,'\nHAVE A NICE DAY')        
         elif y == "3":
            print('you have withdrawn $5,000 you have$',balance - 5000,'\nHAVE A NICE DAY')
         elif y == "4":
            print('you have withdrawn $10,000 you have$',balance - 10000,'\nHAVE A NICE DAY')
         elif y == "5":
            print('you have withdrawn $15,000 you have$',balance - 15000,'\nHAVE A NICE DAY')
         elif y == "6":
            print('you have withdrawn $20,000 you have$',balance - 20000,'\nHAVE A NICE DAY')
         elif y == "7":
            a=int(input('PLEASE INPUT HOW MUCH YOU WOULD LIKE TO WITHDRAW\n'))
            if a <= balance:
                  print ('YOU HAVE WITHDRAWN',a,'you have $',balance-a,'left \nHAVE A NICE DAY' )
            elif a >=balance:
                         print('AMMOUNT TOO HIGH')
#ACCOUNT BALANCE
elif opt=='2':
    print ('YOUR ACCOUNT BALANCE IS $',balance)
#TRANSFER
elif opt== '3':
    w = input('WHAT ACCOUT WOULD YOU BE TRANSFERRING FUNDS TO\n1.FIDELITY BANK,\n2.OTHER BANKS\n')
    if w=='1':
        V=input("TYPE IN BENEFICIARY'S ACCOUNT NUMBER:\n")
        q=int(input("TYPE IN AMMOUNT TO TRANSFER:\n"))
        if q < balance:
            print('you have successfully transferred',balance-q,'to',v,'account')
        elif q >= balance:
            print('INSUFFICIENT FUNDS')
            iput()
    elif w =='2':
        input('TYPE IN THE BANKS NAME:\n')
        p = input('ENTER BEEFICIARIES ACCOUNT NUMBER\n')
        o = eval(input('ENTER AMOUNT TO BE TRANNSFERED,(do not insert a comma)\n'))
        if o < balance:
           print('YOU HAVE SUCCESSFULLY TRANSFERED',o,'to',p,'\nyou have',balance - o,'left')
        else:
            print('INSUFFICIENT FUND')
# BUY_AIRTIME
elif opt=='4':
    k = input('WHAT NETWORK WOULD YOU BE RECHARGING TODAY:\n')
    v = input('THE NUMBER TO BE REACHARGED\n')
    I = int(input('ENTER AMOUNT TO BE RECHARGED\n'))
    print('you have succesfully recharged$',v, 'worth of airtime to', I)
    print('*********PLEASE TAKE YOU CARD**********')
    print('********PLEASE HAVE A NICE DAY*********')
elif opt=='5':
    accName = input("Enter Account name")
    accPin = input("Enter Account pin")
    accVpin = input("Enter Account pin for confirmation")
    accSave = input("Enter the amount you want to deposite")
    if accVpin == accPin:
        print("Account successfully opened")
        vpin.update({accName:accPin})
        balance.update({accName:accSave})
    else:
        print("Pin Mismatch")
else:
    print("wrong input")

input("***************************************************************************************************************************")
     
while reuse > 5:
        reuse = reuse + 1
        print("*******THIS IS A FIDELITY BANK ATM*******")
print("please insert your card")
while counter < maximum:
    pin = input("enter your pin to proceed\n")
    if pin == vpin:
        opt = input("WHAT OPERATION WOULD YOU LIKE TO PERFORM TODAY SIR/MADAM:\n1. Withdrawal\n2. Check balance\n3. Transfer"
                      + "\n4. Buy Airtime\n")
        break
    else:
        counter+=1
        print('incorrect password\n')
        print('you have ',maximum - counter,'tries left\n')
else:
    print ('TOO MANY TRIES COLLECT YOUR CARD')
    input()
 #withdraw
if opt== '1':  
         print("HOW MUCH DO YOU WANT TO WITH")
         y=(input("ENTER:\n1. $1,000   2. $2,000\n3. $5,000"
                       + "   4. $10,000\n5. $15,000  6. $20,000\n7. OTHERS\n"))
         if y == "1": 
                print('you have withdrawn $1,000 you have$',balance - 1000,'\nHAVE A NICE DAY')       
         elif y == "2":
                print('you have withdrawn $2,000 you have$',balance - 2000,'\nHAVE A NICE DAY')        
         elif y == "3":
            print('you have withdrawn $5,000 you have$',balance - 5000,'\nHAVE A NICE DAY')
         elif y == "4":
            print('you have withdrawn $10,000 you have$',balance - 10000,'\nHAVE A NICE DAY')
         elif y == "5":
            print('you have withdrawn $15,000 you have$',balance - 15000,'\nHAVE A NICE DAY')
         elif y == "6":
            print('you have withdrawn $20,000 you have$',balance - 20000,'\nHAVE A NICE DAY')
         elif y == "7":
            a=int(input('PLEASE INPUT HOW MUCH YOU WOULD LIKE TO WITHDRAW\n'))
            if a <= balance:
                  print ('YOU HAVE WITHDRAWN',a,'you have $',balance-a,'left \nHAVE A NICE DAY' )
            elif a >=balance:
                         print('AMMOUNT TOO HIGH')
#ACCOUNT BALANCE
elif opt=='2':
    print ('YOUR ACCOUNT BALANCE IS $',balance)
#TRANSFER
elif opt== '3':
    w = input('WHAT ACCOUT WOULD YOU BE TRANSFERRING FUNDS TO\n1.FIDELITY BANK,\n2.OTHER BANKS\n')
    if w=='1':
        V=input("TYPE IN BENEFICIARY'S ACCOUNT NUMBER:\n")
        q=int(input("TYPE IN AMMOUNT TO TRANSFER:\n"))
        if q < balance:
            print('you have successfully transferred',balance-q,'to',v,'account')
        elif q >= balance:
            print('INSUFFICIENT FUNDS')
            iput()
    elif w =='2':
        input('TYPE IN THE BANKS NAME:\n')
        p = input('ENTER BEEFICIARIES ACCOUNT NUMBER\n')
        o = eval(input('ENTER AMOUNT TO BE TRANNSFERED,(do not insert a comma)\n'))
        if o < balance:
           print('YOU HAVE SUCCESSFULLY TRANSFERED',o,'to',p,'\nyou have',balance - o,'left')
        else:
            print('INSUFFICIENT FUND')
# BUY_AIRTIME
elif opt=='4':
    k = input('WHAT NETWORK WOULD YOU BE RECHARGING TODAY:\n')
    v = input('THE NUMBER TO BE REACHARGED\n')
    I = int(input('ENTER AMOUNT TO BE RECHARGED\n'))
    print('you have succesfully recharged$',v, 'worth of airtime to', I)
    print('*********PLEASE TAKE YOU CARD**********')
    print('********PLEASE HAVE A NICE DAY*********')
else:
    print("wrong input")

input("***************************************************************************************************************************")
     


    
        
    
    





    
                     

