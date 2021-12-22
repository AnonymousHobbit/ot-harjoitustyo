from tkinter import ttk, constants
from modules.task_service import task_service
from modules.user_service import user_service
from visuals.single_task import SingleTaskView


class TaskView:
    def __init__(self, master, control):
        self._root = master
        self._frame = None
        self.control = control
        self._single_task = None
        self._task = None
        self.task_list = None
        self.user_id = user_service.get_id()
        self._initialize()

    def destroy(self):
        self._root.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)

    # Handle new task
    def _add_task(self):
        task = self._task.get()
        task_service.create_new(task, self.user_id)
        self._get_task_list()

    def _remove_task(self, task_id):
        task_service.delete(task_id)
        self._get_task_list()

    # Input field for creating new task
    def _create_new_task(self):
        self._task = ttk.Entry(master=self._frame)
        new_task_button = ttk.Button(
            master=self._frame, text="New Task", command=self._add_task)

        self._task.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=5,
            pady=5,
        )

        new_task_button.grid(
            row=0,
            column=1,
            columnspan=2,
            padx=5,
            pady=5,

        )
        self._frame.grid_columnconfigure(0, weight=1)

    def _back(self):
        self.control.switch_frame("DashboardView")

    def _get_task_list(self):
        self.task_list = task_service.get_by_userid(self.user_id)

        if self._single_task:
            self._single_task.destroy()

        # Single task in the ui
        self._single_task = SingleTaskView(self._root, self)
        self._single_task.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._root.title("Tasks")

        # Set the size of the window at the start
        self._root.geometry("600x400")

        self._create_new_task()
        self._get_task_list()

        self._frame.grid_columnconfigure(0, weight=1)
