import pyautogui
import sys
import logging as log
import threading
import time

# setup logging
format = "%(asctime)s: %(message)s"
log.basicConfig(format=format, level=log.INFO,
                    datefmt="%H:%M:%S")

# hold state to determine if we need to action start/stop commands
state = "STOPPED"
clicker_thread = None
stop_event = threading.Event()

def startClicking():
    global clicker_thread 
    clicker_thread = threading.Thread(target=clicking_thread)
    # make the clicker thread a daemon so it lives and dies with the main application
    clicker_thread.daemon = True
    clicker_thread.start()
    return "RUNNING"

def stopClicking():
    global stop_event
    stop_event.set()
    return "STOPPED"

def clicking_thread():
    global stop_event
    while not stop_event.is_set():
            time.sleep(5) # wait 5 seconds between clicks for now
            pyautogui.click()
    # reset the stop event object
    stop_event = threading.Event()

# get user input
command = input("[" + state + "] Choose from 'start', 'stop', or 'quit'. => ")

# loop until quit is input
while (command != "quit"):
    
    if (command == "start"):
        if (state == "RUNNING"):
            log.info("Already in that state.")
        else:
            state = startClicking()
    elif (command == "stop" and state != "STOPPED"):
        if (state == "STOPPED"):
            log.info("Already in that state.")
        else:
            state = stopClicking()
    elif (command != "start" and command != "stop"):
        log.info("Unknown command.")
    # wait for user input
    command = input("[" + state + "] Choose from 'start', 'stop', or 'quit'. => ")

sys.exit()