
def collectInput():
    title = input("What is the Title of this writeup")
    date = input("Please enter date")
    content = (input("Enter the contents of your diary "))
    
    file = open('diary.txt', 'w')
    file.write(title + '\n'+ date + '\n' +content)
    file = open('diary.txt', 'r')
    
    return title
def verifyCon():
    var_auth = collectInput()

    if var_auth !='':
        print("Diary has been saved successfully")
        print(var_auth)

def updateinput(): 
    title = input("choose the diary you want to update")
    date = input("please enter date")
    content = input("enter the updated content here")
    return title
def verifyupd():
    var_auth = updateinput()

    if var_auth !='':
        print("Diary has been updated successfully")
        print(var_auth)
        
def viewinput():
    title = input("choose the diary you want to view")
def deleteinput ():
    title = input("choose the diary you want to delete")

    return title
def verifydel():
    var_auth = deleteinput()

    if var_auth !='':
        print("Diary has been deleted successfully")
        print(var_auth)


while  True:
    
    
    print("****Daily Diary****")
         
    choice = input("Enteer\n1 -  To write a new diary\n2 - To update an existing diary\n3 - To view the diary\n4 - To delete a diary\n5 - To exit the program")

    if choice == '1':
        verifyCon()
    elif choice == '2':
        verifyupd()
    elif choice == '3':
        choose = input("\nEnter\nA - to view a single diary\nB - to view the entire diary")
        if choose =='A':
            file = open('diary.txt', 'r')
            collect = ''
            for line in file:
                collect += '\n'
                collect += line
            print(collect)
        elif choose == 'B':
            print("a")
        else:
            print("error")
             
    elif choice == '4':
        verifydel()
    elif choice == '5':
        exit()
        
    else:
        print("Invalid selection")


    

