cart = []
while True:
    print("--------------WELCOME TO FLIPKARD------------")
    print("1.LOGIN")
    print("2.REGISTER")
    print("3.EXIT")
    choice = input("----------SELECT YOUR CHOICE-----------")
    if choice == '1':
        user = input("enter your login id")
        pas = input("enter your password")
        if user == login_id and pas == password:
            print(".......LOGIN SUCCESS.........")

            input("......press enter to continue......")
        else:
            print(".....LOGIN FAILED....")
            input("....press enter to continue...")
            continue

        print(".........SHOP NOW MENU........")
        while True:
            print("1.LIST ITEMS")
            print("2.CHECKOUT ITEMS")

            print("3.LIST CART")
            print("4.EXIT")

            choice = int(input("choose option : "))
            itemset = [{'item_id': 1, 'item_name': '1.pen', 'item_price': 10},
                       {'item_id': 2, 'item_name': '2.book', 'item_price': 20},
                       {'item_id': 3, 'item_name': '3.pencil', 'item_price': 5}]

            if choice == 1:
                lis = []
                for value in itemset:
                    lis.append(value['item_name'])
                for i in lis:
                    print(i)
                while True:
                    ch = int(input("choose any item id"))
                    flag = 0
                    for item in itemset:
                        if ch == item["item_id"]:
                            flag = 1
                            cart.append(item)
                            print("cart items are : ", cart)
                        #if flag == 1:
                           # break
                    #if flag == 1:
                            print("item  added to cart")
                            input("press enter to continue shopping or to exit")
                    else:
                        print("item not found")
                        # break
                    break
            elif choice == 2:
                if len(cart) > 0:
                    print("order placed", cart)
                    total = 0
                    for item in cart:
                        total = total + item["item_price"]
                    print("the amount will be : ", total)
                else:
                    print("empty cart")


            #elif choice == 4:
                #print("thanks for visiting us..")
                #break
            elif choice == 3:
                c = int(input("do you want to clear cart(yes or no(1/0)"))
                if c == 1:
                    cart.clear()
                    print("cart cleared", cart)

                    input("press enter to continue")
                elif c == 0:
                    print("cart not cleared",cart)
                    #input("press enter to continue")
                    #break
                    continue
            #else:
            elif choice == 4:
                print("thanks for visiting us..")
                break
            else:
                 break
    elif choice == '2':
        print("......REGISTRATION.........")
        print("...ENTER YOUR DETAILS......")
        login_id = input("enter your name")
        password = input("enter your password")
        pas = input("enter your password again")
        if password != pas:
            print("do not match your password")
        else:
            print("registration completed")
            input(".........press enter to continue......")

    elif choice == '3':
        print("...........you are exited........")
        print(".........THANKS FOR SHOPPING........")
        input(".......press enter to continue......")
