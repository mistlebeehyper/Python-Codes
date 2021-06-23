print("This is program to check for graduating students base on your performance")

subject1 = input("Please enter your first subject\n")

if subject1 == 'Bio' or subject1 == 'Eng' or subject1 == 'Math' or subject1 == 'Chemistry':
       
       score1 = int(input("Please enter your first score\n"))
       if score1 > 50 :
              #print("Congratulation, you are graduating because you passed the test")
              subject2 = input("\nPlease enter your second subject\n")
              if (subject2 == 'Bio' or subject2 == 'Eng' or subject2 == 'Math' or subject2 == 'Chemistry') and subject2 != subject1:
                     score2 = int(input("Please enter your second score\n"))
                     if score2 > 50 :
                            subject3 = input("\nPlease enter your third subject\n")
                            
                     
              else:
                     print("Maths, English and Biology are compulsory subjects and ensure no repetition of entries")
              
       else:
              print("Your score is not up to 50")
       






else:
       print("Maths, English and Biology are compulsory subjects")









       
       score3 = int(input("Please enter your third score\n"))

       subject4 = input("\nPlease enter your forth subject\n")
       score4 = int(input("Please enter your forth score\n"))
       if subject1 == 'Eng' or subject2 == 'Eng' or subject3 == 'Eng' or subject4 == 'Eng':
              if  subject1 == 'Math' or subject2 == 'Math' or subject3 == 'Math' or subject4 == 'Math':
                     if subject1 == 'Chemistry' or subject2 == 'Chemistry' or subject3 == 'Chemistry' or subject4 == 'Chemistry':
                            if subject1 != subject2 and subject2 != subject3 and subject3 != subject4:
                                   if score1 > 50 and score2 >50 and score3 >50 and score4 >50 and ((score1+score2+score3+score4)/4)>60:
                                          print("Congratulation, you are graduating because you passed the test")
                                   else:
                                          print("Either of your score is not up to 50 or your average score is less than 60 ")    
                            else:
                                   print("You have multiple entries of same subject")
                     else:
                            print("Maths, English and Biology are compulsory subjects")
              else:
                     print("Maths, English and Biology are compulsory subjects")
       else:
              print("Maths, English and Biology are compulsory subjects")

                     


