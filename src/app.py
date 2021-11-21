from modules.user import User

def main():
    print("Create user")
    user = User()
    username = input("Username: ")
    password = input("Password: ")
    selection = input("Login (L) / Register (R)")

    if selection.lower() == "r":
        
        print(user.register(username, password))
    elif selection.lower() == "l":

        print(user.login(username, password))
    else:
        print("[!] Invalid selection")
        exit(-1)
    


if __name__ == '__main__':
    main()