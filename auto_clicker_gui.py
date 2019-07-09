import tkinter as tk
import auto_clicker as ac
import re

window = tk.Tk()
window.title("auto-clicker")
window.geometry("400x200")
window.minsize(300, 150)
window.maxsize(400, 200)
validation_regex = r"(?P<time>[\d]+)"  # only capture numbers


def handle_start_stop_press():
    if ((ac.Autoclicker.get_state() == ac.STATE.STOPPED)):
        ac.Autoclicker.start_clicking()
        start_stop_text.set("STOP")
        start_stop_button.configure(bg="red")
    else:
        ac.Autoclicker.stop_clicking()
        start_stop_text.set("START")
        start_stop_button.configure(bg="green")


def click_time():
    """
    Set the click time to a custom value.
    Ignores negative values
    """

    interval_time = get_validated_interval(set_time.get())

    if interval_time != -1:
        ac.Autoclicker.clicking_time = interval_time
        set_time.delete(0, tk.END)
        set_time.insert(0, f"Interval set")
        set_time_button.focus()  # remove blinking cursor by focusing on set time button
    else:
        set_time.delete(0, tk.END)
        set_time.insert(0, "No change")

def get_validated_interval(value):
    """
    takes the raw input from the interval time text field
    returns -1 for invalid input or the validated value to be set
    """

    time = re.search(validation_regex, value)
    if time is not None: 
        return int(time.group()) # cast to int
    
    return -1 # anything that is not a positive int is invalid

start_stop_text = tk.StringVar()
start_stop_text.set("START")
start_stop_button = tk.Button(
    window, textvariable=start_stop_text, command=handle_start_stop_press, bg="green")
start_stop_button.pack(fill=tk.X, padx=5, pady=5, ipadx=20, ipady=20)

time_label = tk.Label(window, text="Autoclick interval: ")
time_label.pack(side=tk.LEFT, )
set_time = tk.Entry(window, width=5, bg="white")
set_time.pack(side=tk.LEFT, padx=5, pady=5, ipadx=18, ipady=5)
set_time_button = tk.Button(window, text="Set", command=click_time, bg="green")
set_time_button.pack(side=tk.RIGHT, padx=5, pady=5, ipadx=70, ipady=5)
set_time.bind("<Button-1>", lambda x: set_time.delete(0, tk.END))  # on left click, delete textbox contents

window.mainloop()
