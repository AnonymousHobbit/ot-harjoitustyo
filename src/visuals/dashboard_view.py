from tkinter import ttk, constants
from modules.user_service import user_service
class DashboardView:
    def __init__(self, root, to_task_view, to_org_view, to_org_create_view):
        self._root = root
        self._frame = None
        self._to_task_view = to_task_view
        self._to_org_view = to_org_view
        self._to_org_create_view = to_org_create_view
        self._user_service = user_service

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._root.geometry("600x400")
        self.main_text = ttk.Label(
            master=self._frame, text=f"Welcome {self._user_service.get_name()}", font=("Helvetica", 16))

        # Check if user belongs to an organisation
        if self._user_service.get_org_name() is not None:
            org_page = ttk.Button(
                master=self._frame, text="Organisation", command=self._to_org_view)
            org_page.grid(row=1, column=0, columnspan=2, pady=5)
        else:
            org_create_page = ttk.Button(
                master=self._frame, text="Create an organisation", command=self._to_org_create_view)
            org_create_page.grid(row=1, column=0, columnspan=2, pady=5)
        private_page = ttk.Button(
            master=self._frame, text="Private tasks", command=self._to_task_view)
        self.main_text.grid(row=0, column=0, columnspan=2)
        
        private_page.grid(row=2, column=0, columnspan=2, pady=5)
        self._frame.pack()
