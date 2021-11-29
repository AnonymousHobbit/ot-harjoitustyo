import sys
from modules.user_service import User
from modules.task_service import Task


def main(user):
    task = Task()
    while True:
        print("\n[*] Select option")
        selection = input(
            "\n[1] Add Task\n[2] View Tasks\n[3] Delete task\n[4] Logout\n")

        if selection == "1":
            task_name = input("\nTask name: ")
            task_desc = input("\nTask description: ")

            if task.create_new(task_name, task_desc, user.get_id()):
                print("[+] Task created")

        elif selection == "2":
            tasks = task.get_by_userid(user.get_id())
            for item in tasks:
                print(f"[{item[0]}] {item[1:]}")

        elif selection == "3":
            task.delete(input("\nTask id: "))

        elif selection == "3":
            print("Logging out...")
            sys.exit()
        else:
            print("[!] Invalid selection")


def login():

    username = input("Username: ")
    password = input("Password: ")
    selection = input("Login (L) / Register (R): ")
    user = User()

    if selection.lower() == "r":
        if user.register(username, password):
            main(user)

    elif selection.lower() == "l":
        if user.login(username, password):
            main(user)
    else:
        print("[!] Invalid selection")
        sys.exit()


if __name__ == '__main__':
    login()
