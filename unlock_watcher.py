import subprocess
from pydbus import SessionBus
from gi.repository import GLib
from config import APP_DIR, VENV_PYTHON

APP_COMMAND = [VENV_PYTHON, "main.py"]

subprocess.Popen(
    [VENV_PYTHON, "-m", "main"],
    cwd=APP_DIR
)

class ScreenListener:
    def __init__(self):
        self.bus = SessionBus()
        self.screensaver = self.bus.get(
            "org.cinnamon.ScreenSaver",
            "/org/cinnamon/ScreenSaver"
        )

        self.screensaver.onActiveChanged = self.on_active_changed

        print("Watcher started — waiting for unlock events...")

    def on_active_changed(self, is_active: bool):
        print("Screen active state changed:", is_active)

        if not is_active:
            print("UNLOCK detected → launching app")
            subprocess.Popen([VENV_PYTHON, "-m", "main"], cwd=APP_DIR)

if __name__ == "__main__":
    listener = ScreenListener()
    GLib.MainLoop().run()