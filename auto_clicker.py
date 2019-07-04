import pyautogui
import threading
import time
import enum

class STATE(enum.Enum):
    STARTED = 1
    STOPPED = 0

class Autoclicker(object):
    state = STATE.STOPPED
    clicker_thread = None
    stop_event = threading.Event()

    @staticmethod
    def startClicking():
        Autoclicker.clicker_thread = threading.Thread(target=Autoclicker.__clicking_thread)
        # make the clicker thread a daemon so it lives and dies with the main application
        Autoclicker.clicker_thread.daemon = True
        Autoclicker.clicker_thread.start()
        Autoclicker.state = STATE.STARTED
        return

    @staticmethod
    def stopClicking():
        Autoclicker.stop_event.set()
        Autoclicker.state = STATE.STOPPED
        return

    @staticmethod
    def getState():
        return Autoclicker.state

    @staticmethod
    def __clicking_thread():
        while not Autoclicker.stop_event.is_set():
            time.sleep(5) # wait 5 seconds between clicks for now
            pyautogui.click()
        # reset the stop event object
        Autoclicker.stop_event = threading.Event()
