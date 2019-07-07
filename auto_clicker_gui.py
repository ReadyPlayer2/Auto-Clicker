import tkinter as tk
import auto_clicker as ac
import re

window = tk.Tk()
window.title("auto-clicker")
window.geometry("400x200")
window.minsize(300, 150)
window.maxsize(400, 200)


def handleStartStopPress():
    if ((ac.Autoclicker.getState() == ac.STATE.STOPPED)):
        ac.Autoclicker.startClicking()
        startStopText.set("STOP")
        startStopButton.configure(bg="red")
    else:
        ac.Autoclicker.stopClicking()
        startStopText.set("START")
        startStopButton.configure(bg="green")


def click_time():
    """
    Set the click time to a custom value.
    Ignores negative values
    """

    click_reg = r"(?P<time>[\d]+)"
    get_time = set_time.get()
    time = re.search(click_reg, get_time)
    if time is not None:  # makde sure a valid time was entered
        ac.Autoclicker.clicking_time = int(time.group())


startStopText = tk.StringVar()
startStopText.set("START")
startStopButton = tk.Button(
    window, textvariable=startStopText, command=handleStartStopPress, bg="green")
startStopButton.pack(fill=tk.X, padx=5, pady=5, ipadx=20, ipady=20)

set_time = tk.Entry(window, width=5, bg="white")
set_time.insert(0, "Enter time between clicks: ")
set_time.pack(side=tk.LEFT, padx=5, pady=5, ipadx=100, ipady=5)
set_time_button = tk.Button(window, text="Set Time",
                            command=click_time, bg="green")
set_time_button.pack(fill=tk.X, padx=5, pady=5, ipadx=20, ipady=20)

window.mainloop()
