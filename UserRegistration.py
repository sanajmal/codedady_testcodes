print("WELCOME TO STUDENT REGISTRATION PORTAL")
def print_options():
    print("Choose Options : \n1.Register\n2.Display\n3.Exit")

while 1:
    print_options()
    user_input = int(input())
    print(type(user_input))
    try:
        if user_input == 1:
            Name = str(input("enter your name:"))
            Age  = int(input("enter your age"))
            if Age<=100:
                print("you are eligible")

                Class = input("class")
                Address = input("enter your address")
                Phone_number = int(input("enter your phone number"))
                if Phone_number <= 10:
                    print("valid")
                else:
                    print("invalid Phone number")
            else:
                print("you are not eligible")
        elif user_input == 2:
            print("display student details")
           # def dislply(self,ob):
                #print("name :", ob.name)
                #print("age :", ob.age)
                #print("address :", ob.address)
                #print("phone_number:", ob.phone_address)
                #print("\n")
        elif user_input ==3:
            print("you are exited")
        else:
            print("Invalid Input")
    except Exception as e:
        print(e)




