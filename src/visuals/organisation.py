from tkinter import ttk, constants
from modules.user_service import user_service
from modules.org_service import OrgService

from visuals.single_task import SingleTaskView


class OrgView:
    """Class of organisation view
        Attributes:
            _root: root of the window
            _frame: frame of the window 
            _single_task: single task view in the ui
            _task: input field for creating new task
            task_list: list of tasks
            org_service: organisation service
            org_name: name of the organisation retrieved from user_service
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
        self._single_task = None
        self._task = None
        self.task_list = None
        self.org_service = OrgService()
        self.org_name = user_service.get_org_name()

        # Initialize the view
        self._initialize()

    def destroy(self):
        """Destroy the window"""
        self._root.destroy()

    def pack(self):
        """Pack the window"""
        self._frame.pack(fill=constants.X)

    # Handle new task
    def _add_task(self):
        task = self._task.get()
        self.org_service.create_task(task, self.org_name)
        self._get_task_list()

    def _leave_org(self):
        user_service.leave_org()
        self._root.destroy()

    def remove_task(self, task_id):
        """Removes the task from the database

        Args:
            task_id: id of the task to be removed
        """
        self.org_service.delete_task(task_id)
        self._get_task_list()

    # Input field for creating new task
    def _create_new_task(self):

        leave_org_button = ttk.Button(
            master=self._frame, text="Leave", command=self._leave_org
        )

        leave_org_button.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.NW
        )

        self._task = ttk.Entry(master=self._frame)
        self._task.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.N
        )

        new_task_button = ttk.Button(
            master=self._frame, text="New Task", command=self._add_task
        )

        new_task_button.grid(
            row=0,
            column=2,
            columnspan=2,
            padx=5,
            pady=5,
            sticky=constants.N

        )

    def _get_task_list(self):
        self.task_list = self.org_service.get_all_tasks(self.org_name)

        if self._single_task:
            self._single_task.destroy()

        # Single task in the ui
        self._single_task = SingleTaskView(self._root, self)
        self._single_task.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._root.title(f"{self.org_name} organisation")
        # Set the size of the window at the start
        self._root.geometry("600x400")
        self._create_new_task()
        self._get_task_list()
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.pack(fill="both")
