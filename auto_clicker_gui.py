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

    click_reg = r"(?P<time>[\d]+)"  # only capture numbers
    get_time = set_time.get()
    time = re.search(click_reg, get_time)
    if time is not None:  # make sure a valid time was entered
        ac.Autoclicker.clicking_time = int(time.group())
        set_time.delete(0, tk.END)
        set_time.insert(0, f"Interval set")
        set_time_button.focus()  # remove blinking cursor by focusing on set time button
    else:
        set_time.delete(0, tk.END)
        set_time.insert(0, "No change")


startStopText = tk.StringVar()
startStopText.set("START")
startStopButton = tk.Button(
    window, textvariable=startStopText, command=handleStartStopPress, bg="green")
startStopButton.pack(fill=tk.X, padx=5, pady=5, ipadx=20, ipady=20)

time_label = tk.Label(window, text="Autoclick interval: ")
time_label.pack(side=tk.LEFT, )
set_time = tk.Entry(window, width=5, bg="white")
set_time.pack(side=tk.LEFT, padx=5, pady=5, ipadx=18, ipady=5)
set_time_button = tk.Button(window, text="Set", command=click_time, bg="green")
set_time_button.pack(side=tk.RIGHT, padx=5, pady=5, ipadx=70, ipady=5)
set_time.bind("<Button-1>", lambda x: set_time.delete(0, tk.END))  # on left click, delete textbox contents

window.mainloop()
