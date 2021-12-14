from tkinter import ttk, constants
from modules.org_service import OrgService
from modules.user_service import user_service
from visuals.organisation import OrgView


class OrgCreateView:
    def __init__(self, master, control):
        self._root = master
        self._frame = None
        self.control = control
        self._org_service = OrgService()
        self._user_service = user_service
        self._org_name = None
        self._org_key = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_create(self):
        org_name = self._org_name.get()
        org_key = self._org_key.get()
        self._org_service.create_new(org_name, org_key, self._user_service)
        self.control.switch_frame(OrgView)

    def _create_new_org(self):

        name_label = ttk.Label(master=self._frame, text="Organisation name")
        self._org_name = ttk.Entry(master=self._frame)

        # Get password as input
        key_label = ttk.Label(master=self._frame, text="Organisation join key")
        self._org_key = ttk.Entry(master=self._frame)

        create_button = ttk.Button(
            master=self._frame, text="Create", command=self._handle_create)


        name_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self._org_name.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        key_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self._org_key.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        create_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=2)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._root.title("Create a new organisation")
        self._root.geometry("600x400")
        self._create_new_org()
        self._frame.grid_columnconfigure(1, weight=0)
