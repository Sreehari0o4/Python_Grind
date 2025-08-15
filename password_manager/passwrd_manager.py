master_passwrd = input("What is the maste password? ")

def add():
    uname = input("Username: ")
    pwd = input("Password: ")
    with open("passwords.txt", 'a') as f:
        f.write(uname + "|" + pwd + "\n")

def view():
    with open("passwords.txt", 'r') as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user, passw = data.split("|")
            print("User:", user, ", Password:", passw)

while True:
    mode = input("Would you like to Add a new password or View passwords (add,view), q to Quit: ")

    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode!")
        continue
