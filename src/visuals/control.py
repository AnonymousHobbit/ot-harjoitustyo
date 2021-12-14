from visuals.mainapp import StartView


class UI:
    def __init__(self, master):
        self._root = master
        self._frame = None

    # Start the application
    def start(self):
        self.switch_frame(StartView)

    # Used to destroy current view
    def _hide(self):
        if self._frame:
            self._frame.destroy()
        self._frame = None

    # Display new frame
    def switch_frame(self, frame):
        self._hide()
        self._frame = frame(self._root, self)
        self._frame.pack()
