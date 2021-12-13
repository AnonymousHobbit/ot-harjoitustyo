from visuals.login_view import LoginView
from visuals.task_view import TaskView
from visuals.register_view import RegisterView
from visuals.start_view import StartView
from modules.user_service import user_service
from visuals.org_view import OrgView
from visuals.org_create_view import OrgCreateView
from visuals.dashboard_view import DashboardView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self.user_service = user_service

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
            to_dashboard_view=self._show_dashboard_view
        )
        self._current_view.pack()

    # Display tasks view
    def _show_tasks_view(self):
        self._hide_current_view()
        self._current_view = TaskView(
            self._root,
            to_org_view=self._show_organisation_view
        )
        self._current_view.pack()

    def _show_register_view(self):
        self._hide_current_view()
        self._current_view = RegisterView(
            self._root,
            to_dashboard_view=self._show_dashboard_view
        )
        self._current_view.pack()

    def _show_organisation_view(self):
        self._hide_current_view()
        self._current_view = OrgView(
            self._root
        )
        self._current_view.pack()

    def _show_dashboard_view(self):
        self._hide_current_view()
        self._current_view = DashboardView(
            self._root,
            to_task_view=self._show_tasks_view,
            to_org_view=self._show_organisation_view,
            to_org_create_view=self._show_create_org_view
        )
        self._current_view.pack()

    def _show_create_org_view(self):
        self._hide_current_view()
        self._current_view = OrgCreateView(
            self._root,
            to_org_view=self._show_organisation_view,
        )
        self._current_view.pack()