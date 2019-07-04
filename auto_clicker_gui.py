import tkinter as tk
import auto_clicker as ac

window = tk.Tk()
window.title("auto-clicker")
window.geometry("400x200")
window.minsize(300, 150)
window.maxsize(400, 200)

def handleStartStopPress():
    if ((ac.Autoclicker.getState() == ac.STATE.STOPPED)):
        ac.Autoclicker.startClicking()
        startStopText.set("STOP")
        startStopButton.configure(bg = "red")
    else:
        ac.Autoclicker.stopClicking()
        startStopText.set("START")
        startStopButton.configure(bg = "green")

startStopText = tk.StringVar()
startStopText.set("START")
startStopButton = tk.Button(window, textvariable=startStopText, command = handleStartStopPress, bg="green")
startStopButton.pack(fill=tk.X, padx=5, pady=5, ipadx=20, ipady=20)

window.mainloop()