from visuals.mainapp import StartView
from visuals.organisation import OrgView
from visuals.org_create import OrgCreateView
from visuals.org_join import OrgJoinView
from visuals.dashboard import DashboardView
from visuals.task import TaskView


class UI:
    def __init__(self, master):
        self._root = master
        self._frame = None
        self.frames = {}

        for F in (StartView, DashboardView, TaskView, OrgCreateView, OrgJoinView, OrgView):
            page_name = F.__name__
            self.frames[page_name] = F

    # Start the application
    def start(self):
        self.switch_frame("StartView")

    # Used to destroy current view
    def _hide(self):
        if self._frame:
            self._frame.destroy()
        self._frame = None

    # Display new frame
    def switch_frame(self, frame):
        self._hide()
        self._frame = self.frames[frame](self._root, self)

        self._frame.pack()
