#create a calculator
#addition
#subtraction
#multiplication
#division


def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    return x / y



while True:


    print("select your operation")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    choice = input("enter the choice 1/2/3/4/5")
    try:
        if choice in ('1','2','3','4'):
            a = float(input("enter first element"))
            b = float(input("enter second element"))
        if choice == '1':
            print(a,"+",b,"=",addition(a,b))
        elif choice == '2':
            print(a,"-",b,"=",subtraction(a,b))
        elif choice == '3':
            print(a,"*",b,"=",multiplication(a,b))
        elif choice == '4':
            print(a,"/",b,"=",division(a,b))
        elif choice == '5':
            print("program exit")
            break
        else:
            print("invalid choice")
    except Exception as e:
        print(e)





