from tkinter import ttk, constants


class RegisterView:
    def __init__(self, root, user_service, to_task_view):
        self._root = root
        self._frame = None
        self._username = None
        self._password = None
        self._to_task_view = to_task_view
        self.user_service = user_service
        self._initialize()

    def _handle_login(self):
        username = self._username.get()
        password = self._password.get()
        if self.user_service.register(username, password):
            self._to_task_view()
        else:
            print("Failed to create a new account")

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        main_text = ttk.Label(
            master=self._frame, text="Create a new account", font=("Helvetica", 16))

        # Set the size of the window at the start
        self._root.geometry("600x400")

        # Get username as input
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username = ttk.Entry(master=self._frame)

        # Get password as input
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame, text="Register", command=self._handle_login)

        # vasempaan laitaan
        main_text.grid(row=0, column=0, padx=5, pady=25, columnspan=2)

        username_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self._username.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        password_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self._password.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        login_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=2)
