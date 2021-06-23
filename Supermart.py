from datetime import datetime

x = 0
y = 0
total = 0
index = 0
counter = 0
counter2 = 0
maximum = 3

price_product = {"Groundnuts" :2.00, "Cashewnuts" :6.00, "Pea__nuts" :2.50, "RipeP-chips" :2.00, "UnripeP-chips" :2.50, "Coconut-chips" :3.00, "Potato-chips" :2.50, "Chin__Chin" :2.00, "Salted-popcorn" :2.50, "Sugary-popcorn" :2.50}
quantity_product = {"Groundnuts" :57, "Cashewnuts" :42, "Pea__nuts" :56, "RipeP-chips" :88, "UripeP-chips" :75, "Coconut Chips" :69, "Potato Chips" :78, "Chin-Chin" :83, "Salted Popcorn" :57, "Sugary Popcorn" :58}
people_access = {"Store Owner" :"Mrs. Wendy WHITE", "Store Manager" :"Mr. Ben KUMASI", "Checker 1" :"Miss. Moriofe NNEDNA", "Checker 2" :"Mr. Richard UNAME", "Checker 3" :"Mr. David CHIJIOKE", "Checker 4" :"Miss Eseose IMEHE", "Checker 5" :"Mr. Samuel OGUNE", "Checker 6" :"Mrs. Chisom OPKALA"}
passwrd_access = {"Store Owner" :"WmW5s", "Store Manager" :"BmK3r", "Checker 1" :"MmN7m", "Checker 2" :"RmU7r", "Checker 3" :"DmC5r", "Checker 4" :"EmI6m", "Checker 5" :"SmO6r", "Checker 6" :"CmO6s"}

def set_word():
    global total, index
    re = []
    cart = []
    index = 0
    total = 0

def passwrd():
    try:
        global counter
        global counter2
        while counter < maximum:
            name = input("Please input your name; E.g Mrs. Danladi BROWN: ")
            position = input("Please input your emloyment status; E.g Checker 10: ")
            pin = input("Please input your password: ")
            if pin == passwrd_access[position]:
                break
            else:
                counter == counter + 1
                print("Incorrect password.")
                passwrd()
        else:
            if counter == maximum:
                counter = counter + 1
                print("Too many tries. Goodbye...")

        while counter2 < maximum:
            if name == people_access[position]:
                options()
            else:
                counter2 = counter2 + 1
                print("Name does not match with password.")
                passwrd()
        else:
            if counter2 == maximum:
                counter2 = counter2 + 1
                print("Too many tries goodbye...")
                input()
    except:
        print("Invalid 'Employment Status'")
        passwrd()

def options():
    do = input("What function would you like to perform:\n 1. View Price and Quantity lists of products.\n 2. Manipulate Price and Quantity lists of products.\n 3. Take a customers order.\n : ")
    if do == "1":
        view()
    elif do == "2":
        add_update()
    elif do == "3":
        orderA()
    elif do == "4":
        quit()
    else:
        print("Invalid option.")
        options()

def add_update():
    do_you = input("Do you wish to:\n 1. Update the the food items lists(Both Price and Quantity).\n 2. Change the food items lists(Both Price and Quantity).\n : ")
    if do_you == "1":
        update()
    elif do_you == "2":
        add()
    else:
        print("Invalid option.")
        add_update()

def update():
    name = input("Please input the name of the product to be added: ")
    price = input("Please input the price of the product to be added: ")
    quantity = input("Please input the quantity of the product to be added: ")
    price_product.update({name: price})
    quantity_product.update({name: quantity})
    list1 = price_product[name]
    list2 = quantity_product[name]
    print("This is your current update| Product:",name,"; Price:",list1)
    print("This is your current update| Product:",name,"; Quantity:",list2)
    input("Press Enter")
    again = input("Do you wish to:\n 1. Perform this function again.\n 2. Go back to the main menu.\n 3. Quit this program.\n : ")
    if again == "1":
        update()
    elif again == "2":
        options()
    else:
        quit()

def add():
    global x
    print("This function would remove all the items before allowing you added items afresh.\nPlease note that after all changes the product names in your 'Price' and 'Quantity' lists should tally")
    opt = input("Do you want to change the:\n 1. Price lists\n 2. Quantity lists\n : ")
    if opt == "1":
        price_product.clear()
        how = int(input("How many product prices do you wish to enter?: "))
        while x < how:
            x = x + 1
            name = input("Please input the name of the product to be added: ")
            price = input("Pplease input the price of the product stated: ")
            price_product.update({name: price})
        #print("This is your new price list",price_product.items())
        print("PRODUCT \t|\t PRICE($)")
        for c in price_product.items():
            print(f"{c[0]} \t|\t {c[1]}")
            
        input("Press Enter")
        again = input("Do you wish to:\n 1. Perform this function again.\n 2. Go back to the main menu.\n 3. Quit this program.\n : ")
        if again == "1":
            add()
        elif again == "2":
            options()
        else:
            quit()
            
    elif opt == "2":
        quantity_product.clear()
        how2 = int(input("How many product quantities do you wish to enter?: "))
        while x < how2:
            x += 1
            name2 = input("Please input the name of the product to be added: ")
            quantity = input("Please input the price of the product stated: ")
            price_product.update({name2: quantity})
            #print("This is your new quantity list",quantity_product.items())
        input("Press Enter")
        print("PRODUCT \t|\t QUANTITY(packs)")
        for d in price_product.items():
            print(f"{d[0]} \t|\t {d[1]}")

    else:
        print("Invalid option.")
        add()

def view():
    do = input("Do you wish to view:\n 1. Quantity list.\n 2. Price list.\n : ")
    if do == "1":
        #print("This is the current quantity list|",quantity_product.items())
        print("PRODUCT \t|\t QUANTITY(packs)")
        for q in quantity_product.items():
            print(f"{q[0]} \t|\t {q[1]}")
    elif do == "2":
        #print("This is the current price list|",price_product.items())
        print("PRODUCT \t|\t PRICE($)")
        for w in price_product.items():
            print(f"{w[0]} \t|\t {w[1]}")
    else:
        print("Invalid option.")
        view()
    again = input("Do you wish to:\n 1. Perform this function again.\n 2. Go back to the main menu.\n 3. Quit this program.\n : ")
    if again == "1":
        view()
    elif again == "2":
        options()
    else:
        quit()

#def discount():
    #global total
    #d = datetime.now()
    #m = d.month
    #if month == 3:
        #print("You have a discount of 10%.")
        #secTotal = 0.1*total
        #print(f"\nTotal Cost: ${secTotal}\n")
    #else:
        #print(f"\nTotal Cost: ${total}\n")

def orderA():
    global index, y, total
    name = input("Please input customers name: ")
    order = input("Please input the customers's order: ")
    quantity_items = input("Please input how many of each items will be bought: ")
    quantity_items = quantity_items.split()
    re = []
    for i in quantity_items:
        re.append(int(i))
    order = order.split()
    input("Press Enter\n")

    cart = []
    while index<len(order):
        item_name = order[index]
        qty = re[index]
        unit_price = price_product[order[index]]
        cost = qty * unit_price
        index += 1
        total += cost
        cart.append(f'{item_name}\t{qty} packs\t\t{unit_price}\t\t{cost}')
    d = datetime.now()
    m = d.month
    s = d.day
    if m == 12 or m == 11:
        print("You have a discount of 10%.")
        secTotal = 0.9*total
        print(f"\nTotal Cost: ${secTotal}\n")
        input("Press Enter: ")

        print("\n\t>>>RECEIPT<<<")
        print(">>>>>WENDY's CHIPS, CHOPS and NUTS<<<<<")
        print("Name:",name)
        print(datetime.now().ctime())
        print("-----Item(s) Bought-----")
        print("ITEM_NAME\tQUANTITY\tPRICE($)\t\tSUBTOTAL($)")
        for s in cart:
            print(s)
        sT = 0.1*total
        print("You are given a 10% discount because it is a festive season.")
        print(f"\nDiscount: ${sT}")
        print(f"Total: ${secTotal}\n")
        print("Thanks for shopping with us!\n\t Please do call again...\nGoods bought in good condition cannot be returned.\n\t\t For more enquiries email us: wendy_foods@gmail.com")


    else:
        if 1000 <= total < 2000:
            decTotal = 0.9*total
            print(f"\nTotal Cost: ${decTotal}\n")    
            input("Press Enter: ")
        
            print("\n\t>>>RECEIPT<<<")
            print(">>>>>WENDY's CHIPS, CHOPS and NUTS<<<<<")
            print("Name:",name)
            print(datetime.now().ctime())
            print("-----Item(s) Bought-----")
            print("ITEM_NAME\tQUANTITY\tPRICE($)\t\tSUBTOTAL($)")
            for s in cart:
                print(s)
            r = 0.1*total
            print("Initial Cost:",total)
            print("Since you have spent over $1000, you are given a 10% discount.")
            print(f"\nDiscount: ${r}")
            print(f"Total: ${decTotal}\n")
            print("Thanks for shopping with us!\n\t Please do call again...\nGoods bought in good condition cannot be returned.\n\t\t For more enquiries email us: wendy_foods@gmail.com")

        elif 2000 <= total < 3000:
            decTotal2 = 0.8*total
            print(f"\nTotal Cost: ${decTotal2}\n")    
            input("Press Enter: ")
        
            print("\n\t>>>RECEIPT<<<")
            print(">>>>>WENDY's CHIPS, CHOPS and NUTS<<<<<")
            print("Name:",name)
            print(datetime.now().ctime())
            print("-----Item(s) Bought-----")
            print("ITEM_NAME\tQUANTITY\tPRICE($)\t\tSUBTOTAL($)")
            for s in cart:
                print(s)
            r2 = 0.2*total
            print("Initial Cost:",total)
            print("Since you have spent over $2000, you are given a 20% discount.")
            print(f"\nDiscount: ${r2}")
            print(f"Total: ${decTotal2}\n")
            print("Thanks for shopping with us!\n\t Please do call again...\nGoods bought in good condition cannot be returned.\n\t\t For more enquiries email us: wendy_foods@gmail.com")

        elif 3000 <= total < 4000:
            decTotal3 = 0.7*total
            print(f"\nTotal Cost: ${decTotal3}\n")    
            input("Press Enter: ")
        
            print("\n\t>>>RECEIPT<<<")
            print(">>>>>WENDY's CHIPS, CHOPS and NUTS<<<<<")
            print("Name:",name)
            print(datetime.now().ctime())
            print("-----Item(s) Bought-----")
            print("ITEM_NAME\tQUANTITY\tPRICE($)\t\tSUBTOTAL($)")
            for s in cart:
                print(s)
            r3 = 0.3*total
            print("Initial Cost:",total)
            print("Since you have spent over $3000, you are given a 30% discount.")
            print(f"\nDiscount: ${r3}")
            print(f"Total: ${decTotal3}\n")
            print("Thanks for shopping with us!\n\t Please do call again...\nGoods bought in good condition cannot be returned.\n\t\t For more enquiries email us: wendy_foods@gmail.com")            

        elif 4000 <= total < 5000:
            decTotal4 = 0.6*total
            print(f"\nTotal Cost: ${decTotal4}\n")    
            input("Press Enter: ")
        
            print("\n\t>>>RECEIPT<<<")
            print(">>>>>WENDY's CHIPS, CHOPS and NUTS<<<<<")
            print("Name:",name)
            print(datetime.now().ctime())
            print("-----Item(s) Bought-----")
            print("ITEM_NAME\tQUANTITY\tPRICE($)\t\tSUBTOTAL($)")
            for s in cart:
                print(s)
            r4 = 0.4*total
            print("Initial Cost:",total)
            print("Since you have spent over $4000, you are given a 40% discount.")
            print(f"\nDiscount: ${r4}")
            print(f"Total: ${decTotal4}\n")
            print("Thanks for shopping with us!\n\t Please do call again...\nGoods bought in good condition cannot be returned.\n\t\t For more enquiries email us: wendy_foods@gmail.com")

        elif 5000 <= total:
            decTotal5 = 0.5*total
            print(f"\nTotal Cost: ${decTotal5}\n")    
            input("Press Enter: ")
        
            print("\n\t>>>RECEIPT<<<")
            print(">>>>>WENDY's CHIPS, CHOPS and NUTS<<<<<")
            print("Name:",name)
            print(datetime.now().ctime())
            print("-----Item(s) Bought-----")
            print("ITEM_NAME\tQUANTITY\tPRICE($)\t\tSUBTOTAL($)")
            for s in cart:
                print(s)
            r5 = 0.5*total
            print("Initial Cost:",total)
            print("Since you have spent over $5000, you are given a 50% discount.")
            print(f"\nDiscount: ${r5}")
            print(f"Total: ${decTotal5}\n")
            print("Thanks for shopping with us!\n\t Please do call again...\nGoods bought in good condition cannot be returned.\n\t\t For more enquiries email us: wendy_foods@gmail.com")

    input("Press Enter")
    set_word()

    again = input("Do you wish to:\n 1. Perform this function again.\n 2. Go back to the main menu.\n 3. Quit this program.\n : ")
    if again == "1":
        orderA()
    elif again == "2":
        options()
    else:
        quit()
        


try:
    print(">>>>>WENDY's CHIPS, CHOPS and NUTS<<<<<")
    passwrd()
except:
    print("\tCode Error...\n Please restart this program.")
    input("Press Enter")
    passwrd()

