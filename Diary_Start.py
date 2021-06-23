def collectInput():
       title = input("What is the title for this write up")
       date = input("DATE")
       content = input("Write up...")

       return title

def verifyCon():
       var_auth = collectInput()

       if var_auth != '':
             print("Diary has been saved successfully")
             print(var_auth)


print("****Daily Diary****")

choice = input("Enter\n1 - To write a new diary\n2 - To update an existing diary\n")

if choice == '1':
       verifyCon()
elif choice == '2':
       #statement
       print("here is for updating a diary")
else:
       print("Enter the right option")
