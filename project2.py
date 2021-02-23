def addData():
    pass


data_list = []
id_list = []
while True:
    print("--------- PERSON DETAILS-------- ")
    print("1.LOGIN")
    print("2.REGISTER")
    print("3.LIST USERS")
    print("4.EXIT")
    choice = input("--------SELECT YOUR CHOICE--------")
    if choice == '1':
        #user = input("enter your login id")
        #pas = input("enter your password")
        #if user == login_id and pas == password:
            #print("----LOGIN SUCCESS---")
            #input(".........press enter to continue........")
        #else:
            #print("-----LOGIN FAILED-----")
            #input(".........press enter to continue........")
            #continue
        while True:

                name = input("ENTER YOUR USER NAME")
                if name.isalpha():
                    break
        while True:

                id = input("ENTER YOUR PASSWORD")
                if password.isalpha():
                    break

        data = {}
        data["name"] = name
        data["password"] = password
        print("data : ", data)
        data_list.append(data)
        id_list.append(data)
        input("added successfully, press enter to continue")
        #print("peoples are : ", data_list)
        print("peoples are..........")
        print(data_list)
        #print("items are : ", id_list)

    if choice == '2':
        print("......REGISTRATION.......")
        print(".........ENTER YOUR DETAILS..........")
        login_id = input("enter your name")
        password = input("enter your password")
        pas = input("enter your password again")
        if password != pas:
            print("do not match your password")
        else:
            print("registration completed")
            input(".........press enter to continue......")

    elif choice == '3':
        #data_list = []
        #for value in data_list:
            #data_list.append(value['name','password'])
        #for i in data:
            #data = input()
        #data_list.append(data)
        print(data_list)
            #print(i)


    elif choice == '4':

        print("...........you are exited........")
        print(".........THANKS FOR SHOPPING........")
        input(".......press enter to continue......")
