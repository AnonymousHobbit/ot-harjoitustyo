from tkinter import ttk, messagebox
from modules.user_service import user_service, IncorrectCredentialsError, UsernameExistsError


class StartView:
    def __init__(self, master, control):
        self._root = master
        self._frame = None
        self.username = None
        self.password = None
        self.control = control
        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack()

    # Handle creating new account
    def _handle_register(self):
        username = self._username.get()
        password = self._password.get()
        try:
            user_service.register(username, password)
            self.control.switch_frame("DashboardView")
        except UsernameExistsError:
            messagebox.showerror("Error", "Username already exists")

    # Handle login to already existing account
    def _handle_login(self):
        username = self._username.get()
        password = self._password.get()
        try:
            user_service.login(username, password)
            self.control.switch_frame("DashboardView")
        except IncorrectCredentialsError:
            messagebox.showerror("Error", "Incorrect username or password")

    def _initialize(self):
        # Main windows configuration
        self._frame = ttk.Frame(master=self._root)
        self._root.geometry("600x400")

        # Label
        main_text = ttk.Label(master=self._frame,
                              text="Login or create a new account",
                              font=("Helvetica", 16)
                              )
        main_text.grid(row=0, column=0, padx=5,
                       pady=25, columnspan=2)

        # Username section
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username = ttk.Entry(master=self._frame)
        username_label.grid(row=1, column=0, columnspan=2,
                            padx=5, pady=5)
        self._username.grid(row=2, column=0, columnspan=2,
                            padx=5, pady=5, ipadx=30)

        # password section
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password = ttk.Entry(master=self._frame)
        password_label.grid(row=3, column=0, columnspan=2,
                            padx=5, pady=5)
        self._password.grid(row=4, column=0, columnspan=2,
                            padx=5, pady=5, ipadx=30)

        # Login button
        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._handle_login)
        login_button.grid(row=5, column=0, columnspan=2,
                          padx=5, pady=5, ipadx=60)

        # Register button
        register_button = ttk.Button(
            master=self._frame, text="Register", command=self._handle_register)
        register_button.grid(row=6, column=0, columnspan=2,
                             padx=5, pady=5, ipadx=60)

        self._frame.grid_columnconfigure(0, weight=1)
