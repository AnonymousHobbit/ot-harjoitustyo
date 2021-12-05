from tkinter import Tk
from visuals.main import UI


def main_menu():
    window = Tk()
    window.title("Task manager V2.0")

    user_interface = UI(window)
    user_interface.start()

    window.mainloop()


if __name__ == '__main__':
    main_menu()
