import os
from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


if not os.path.exists("key.key"):
    write_key()

key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            acc_name, pwd = data.split("|")
            print(
                "Account Name: ",
                acc_name,
                "| Password: ",
                fer.decrypt(pwd.encode()).decode(),
            )


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Enter the mode(View/Add/Quit): ").lower()
    if mode == "quit":
        quit()

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Try again")
        continue
