from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def add():
    uname = input("Username: ")
    pwd = input("Password: ")
    with open("passwords.txt", 'a') as f:
        f.write(uname + "|" + (fer.encrypt(pwd.encode())).decode() + "\n")

def view():
    with open("passwords.txt", 'r') as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user, passw = data.split("|")
            print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())

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
