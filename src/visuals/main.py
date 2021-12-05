from visuals.login_view import LoginView
from visuals.task_view import TaskView
from visuals.register_view import RegisterView
from visuals.start_view import StartView
from modules.user_service import UserService


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self.user_service = UserService()

    def start(self):
        self._current_view = StartView(
            self._root,
            to_login_view=self._show_login_view,
            to_register_view=self._show_register_view
        )
    # Used to destroy current view

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    # Display login view
    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(
            self._root,
            user_service=self.user_service,
            to_task_view=self._show_tasks_view
        )
        self._current_view.pack()

    # Display tasks view
    def _show_tasks_view(self):
        self._hide_current_view()
        self._current_view = TaskView(
            self._root,
            user_service=self.user_service
        )
        self._current_view.pack()

    def _show_register_view(self):
        self._hide_current_view()
        self._current_view = RegisterView(
            self._root,
            user_service=self.user_service,
            to_task_view=self._show_tasks_view
        )
        self._current_view.pack()
