from tkinter import ttk, constants

class OrgView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._root.title("Your organisation")
        self._root.geometry("600x400")
        self._frame.grid_columnconfigure(1, weight=0)
