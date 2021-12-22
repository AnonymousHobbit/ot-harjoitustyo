from tkinter import ttk
from modules.user_service import user_service


class DashboardView:
    """Class of Dashboard view
    
    Attributes:
        _root: root window
        _frame: frame of dashboard view

    """
    def __init__(self, master, control):
        """Constructor that initializes the window
        
        Args:
            master: root window
            control: control.py class instance
        """
        self._root = master
        self._frame = None
        self.control = control
        self._initialize()

    def destroy(self):
        """Destroy the window"""
        self._frame.destroy()

    def pack(self):
        """Pack the window"""
        self._frame.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._root.geometry("600x400")
        self.main_text = ttk.Label(
            master=self._frame, text=f"Welcome {user_service.get_name()}",
            font=("Helvetica", 16))
        self.main_text.grid(row=0, column=0, columnspan=2)

        # Check if user belongs to an organisation
        if user_service.get_org_name() is not None:
            org_page = ttk.Button(
                master=self._frame, text="Organisation",
                command=lambda: self.control.switch_frame("OrgView"))
            org_page.grid(row=1, column=0, columnspan=2, pady=5)
        else:
            org_join_page = ttk.Button(
                master=self._frame, text="Join an organisation",
                command=lambda: self.control.switch_frame("OrgJoinView"))

            org_join_page.grid(row=1, column=0, columnspan=2, pady=5)

            org_create_page = ttk.Button(
                master=self._frame, text="Create an organisation",
                command=lambda: self.control.switch_frame("OrgCreateView"))
            org_create_page.grid(row=2, column=0, columnspan=2, pady=5)

        private_page = ttk.Button(
            master=self._frame, text="Private tasks",
            command=lambda: self.control.switch_frame("TaskView"))

        private_page.grid(row=3, column=0, columnspan=2, pady=5)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.pack()
