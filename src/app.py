from tkinter import Tk
from visuals.control import UI


if __name__ == '__main__':
    window = Tk()
    window.title("Task manager V2.0")

    # Start the app
    ui = UI(window)
    ui.start()

    window.mainloop()
