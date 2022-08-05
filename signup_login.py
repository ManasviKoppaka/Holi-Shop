def hr():
    print("-----------------------------------------------")
def hr2():
    print("_______________________________________________")
def hr3():
    print("***********************************************")


def signup():
    hr2()
    print("Welcome! Enter the following details to set up your account")
    hr()
    username = input("Enter the username: ")
    if username == "":
        print("Invalid username. Try Again")
        return
    db = open("DataBase.txt", "r")
    for data in db:
        u,p = data.split(",")
        if username == u:
            print("Username has already been used. Try Again")
            return
    db.close()

    
    password = input("Enter the password. It must contain minimum 5 characters, a capital letter, a special character (@, #, *, !) and a number")
    special = ["@", "#", "*", "!"]
    if len(password) < 5:
        print("The password must contain atleast 5 characters. Try Again")
        signup()
    cap = False
    for i in password:
        if i.isupper():
            cap = True
            break
    if cap == False:
        print("The password must contain atleast 1 capitalized character. Try Again")
        return 

    sp = False
    for i in special:
        if i in password:
            sp = True
            break
    if sp == False:
        print("The password must contain atleast 1 special character. Try Again")
        return 

    num = False
    for i in password:
        if i.isnumeric():
            num = True 
            break
    if num == False:
        print("The password must contain atleast 1 number. Try Again")
        return

    confirm_password = input("Enter your password again: ")
    if password != confirm_password:
        print("The password and confirm password are not matching. Try Again ")
        return


    data = username + "," + password
    db = open("DataBase.txt", "a")
    db.write(data)
    db.write("\n")
    db.close()
    hr2()
    print("Your account has been created succesfully!")
    hr2()
    return


def login():
    print("Welcome Back! Please enter the following details to log in succesfully")
    username = input("Enter your username: ")
    db = open("DataBase.txt", "r")
    flag = 0
    for i in db:
        u,p = i.split(",")
        if username == u:
            flag = 1
            break
    db.close()
    if flag == 0:
        print("Username doesn't exist. Try Again")
        return
    password = input("Enter your password: ")
    hr()
    password = password+"\n"
    if password != p:
        print("Incorrect Password. Try Again")
        return False
    hr2()
    print("Login Succesfull!")
    hr2()
    return username
    # db = open("DataBase.txt", "r")
    # for i in db:
    #     print(i)
    # input("Press Enter to log out")
#Main Program
