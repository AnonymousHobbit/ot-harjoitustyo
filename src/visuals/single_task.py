from tkinter import ttk, constants


class SingleTaskView:
    def __init__(self, master, parent):
        self._root = master
        self.parent = parent
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _task_frame(self, item):
        task_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=task_frame, text=item[1])
        label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)

        del_task_button = ttk.Button(
            master=task_frame, text="Delete", command=lambda: self.parent.remove_task(item[0]))

        del_task_button.grid(row=1, column=1, padx=5,
                             pady=5)

        task_frame.grid_columnconfigure(0, weight=1)
        task_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(self._root)

        # Frame for each task
        tasks = self.parent.task_list
        for item in tasks:
            self._task_frame(item)
