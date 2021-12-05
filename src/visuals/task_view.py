from tkinter import ttk, constants
from modules.task_service import TaskService


class SingleTask:
    def __init__(self, root, task_list):
        self._root = root
        self._task_list = task_list
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(self._root)
        # Frame for each task
        for item in self._task_list:
            task_frame = ttk.Frame(master=self._frame)
            label = ttk.Label(master=task_frame, text=item[1])
            label.grid(row=1, column=0, padx=5, pady=5)
            task_frame.grid_columnconfigure(0, weight=1)
            task_frame.pack(fill=constants.X)


class TaskView:
    def __init__(self, root, user_service):
        self._root = root
        self._frame = None
        self._task_service = TaskService()
        self._user_service = user_service
        self._single_task = None
        self._task = None

        self._initialize()

    def destroy(self):
        self._root.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)

    # Handle new task
    def _add_task(self):
        task = self._task.get()
        user_id = self._user_service.get_id()
        self._task_service.create_new(task, user_id)
        self._get_task_list()

    # Input field for creating new task

    def _create_new_task(self):
        self._task = ttk.Entry(master=self._frame)
        new_task_button = ttk.Button(
            master=self._frame, text="New Task", command=self._add_task)

        self._task.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        new_task_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _get_task_list(self):
        user_id = self._user_service.get_id()
        task_list = self._task_service.get_by_userid(user_id)
        if self._single_task:
            self._single_task.destroy()
        self._single_task = SingleTask(self._root, task_list)
        self._single_task.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._root.title("Tasks")
        # Set the size of the window at the start
        self._root.geometry("600x400")

        self._create_new_task()
        self._get_task_list()
