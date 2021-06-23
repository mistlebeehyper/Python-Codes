import random
playersName= []
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
list8=[]
list9=[]
list10=[]
x= 0
a= 0
randomNo = 0

print("*****This is a guess game*****")
noOfPlayers = int(input("How many players will like to play this game"))

while x < noOfPlayers:
       colname = input("Please enter your name")
       playersName.append(colname)
       x= x+1

while True:
       while a < len(playersName):
              while True:
                     print(playersName[a])
                     randomNo = random.randint(1,10)
                     playerAns = int(input("What did I write"))
                     if randomNo == playerAns:
                     
                            if randomNo == 1:
                                   if len(list1)< 1:
                                          list1.append(randomNo)
                                   else:
                                          print("slot filled")
                                          break
                            
                            elif randomNo == 2:
                                   if len(list2)< 2:
                                          list2.append(randomNo)
                                   else:
                                          print("slot filled")
                                          break
                                   
                            elif randomNo == 3:
                                   if len(list3)< 3:
                                          list3.append(randomNo)
                                   else:
                                          print("slot filled")
                                          break
                                   
                            elif randomNo == 4:
                                   if len(list4)< 3:
                                          list4.append(randomNo)
                                   else:
                                          print("slot filled")
                                          break
                                   
                            elif randomNo == 5:
                                   if len(list5)< 5:
                                          list5.append(randomNo)
                                   else:
                                          print("slot filled")
                                          break
                                   
                            elif randomNo == 6:
                                   if len(list6)< 6:
                                          list6.append(randomNo)
                                   else:
                                          print("slot filled")
                                          break
                                   
                            elif randomNo == 7:
                                   if len(list7)< 7:
                                          list7.append(randomNo)
                                   else:
                                          print("slot filled")
                                          break
                                   
                            elif randomNo == 8:
                                   if len(list8)< 8:
                                          list8.append(randomNo)
                                   else:
                                          print("slot filled")
                                          break
                                   
                            elif randomNo == 9:
                                   if len(list9)< 9:
                                          list9.append(randomNo)
                                   else:
                                          print("slot filled")
                                          break
                                   
                            elif randomNo == 10:
                                   if len(list10)< 10:
                                          list10.append(randomNo)
                                   else:
                                          print("slot filled")
                                          break
                                   
                            else:
                                   print("Entry out of range")
                     else:
                            print("Wrong")
                            break
              a = a + 1
              if a == len(playersName):
                     a= 0
              
                     
                     
              
              
       


