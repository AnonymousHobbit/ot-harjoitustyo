from tkinter import ttk, messagebox
from modules.org_service import OrgService
from modules.user_service import InvalidJoinKeyError, user_service, InvalidJoinKeyError


class OrgJoinView:
    """Class of join organisation view
    
    Attributes:
        _root: root of the window
        _frame: frame of the window
        _org_name: input field for organisation name
        _org_key: input field for organisation join key
        _org_service: organisation service
    
    """

    def __init__(self, master, control):
        """Constructor that initalizes the window
        
        Args:
            master: root of the window
            control: control.py class instance
        """
        self._root = master
        self._frame = None
        self.control = control
        self._org_service = OrgService()
        self._org_name = None
        self._org_key = None
        self._initialize()

    def destroy(self):
        """Destroy the window"""
        self._frame.destroy()

    def pack(self):
        """Pack the window"""
        self._frame.pack()

    

    def _handle_join(self):
        org_name = self._org_name.get()
        org_key = self._org_key.get()
        try:
            user_service.join_org(org_name, org_key)
            self.control.switch_frame("OrgView")
        except InvalidJoinKeyError:
            messagebox.showerror("Error", "Invalid join key")

    def _create_new_org(self):

        # Name section
        name_label = ttk.Label(master=self._frame, text="Organisation name")
        self._org_name = ttk.Entry(master=self._frame)
        name_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self._org_name.grid(row=2, column=0, columnspan=2,
                            padx=5, pady=5, ipadx=30)

        # Join key section
        key_label = ttk.Label(master=self._frame, text="Organisation join key")
        self._org_key = ttk.Entry(master=self._frame)
        key_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self._org_key.grid(row=4, column=0, columnspan=2,
                           padx=5, pady=5, ipadx=30)

        # Join button
        join_button = ttk.Button(
            master=self._frame, text="Join", command=self._handle_join)
        join_button.grid(row=5, column=0, columnspan=2,
                           padx=5, pady=5, ipadx=60)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._root.title("Join to an organisation")
        self._root.geometry("600x400")
        self._create_new_org()
        self._frame.grid_columnconfigure(0, weight=1)
