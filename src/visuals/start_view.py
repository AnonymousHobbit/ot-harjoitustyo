from tkinter import ttk, constants


class StartView:
    def __init__(self, root, to_register_view, to_login_view):
        self._root = root
        self._frame = None
        self._to_register_view = to_register_view
        self._to_login_view = to_login_view

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._root.geometry("600x400")
        self.main_text = ttk.Label(
            master=self._frame, text="Welcome back!", font=("Helvetica", 16))
        register_page = ttk.Button(
            master=self._frame, text="Create an account", command=self._to_register_view)
        login_page = ttk.Button(
            master=self._frame, text="Login to an existing account", command=self._to_login_view)
        self.main_text.grid(row=0, column=0, columnspan=2)
        register_page.grid(row=1, column=0, columnspan=2, pady=5)
        login_page.grid(row=2, column=0, columnspan=2, pady=5)
        self._frame.pack()
