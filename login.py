class login:
    # def __init__(self,id,pas)
    # self.id = "admin"
    # self.pas = "admin"

    def check(self,id,pas):
        #print(self.id)
        #print(self.pas)

        if(id == "admin" and pas == "123"):
            print("login success!")
        else:
            print("incorrect password and username")

log_obj = login()

print("----login page-----")
log = input("Enter Login ID:")
print(log)

pasw = input("Enter password:")
log_obj.check(log,pasw)
