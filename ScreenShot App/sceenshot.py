# First we have to install virtualenv
# Type in cmd the command : pip install virtualenv

import time
import pyautogui
import tkinter as tk

# The function that takes screenshots
def screenshot():
    # Using the time function we will generate an int number
    name = int(round(time.time() * 1000))

    # The path of the sceenshots data file
    # You can change it with your own file path
    path = 'G:/Github projects/Python projects/SomePython/ScreenShot App/screenshots data'

    # Setting the name
    name = '{}/{}.png'.format(path, name)

    # Wait 5 seconds
    # time.sleep(5)

    # Use the pyautogui function screenshot()
    img = pyautogui.screenshot(name)

    # Show the screenshot
    img.show()

# screenshot()

root = tk.Tk()
frame = tk.Frame(root)

w = tk.Label(root, text="Hello !")
w.pack()

frame.pack()



# Create button
button = tk.Button(
    frame,
    text = "Take screenshot",
    command = screenshot
)

# Place the Take Screenshot button
button.pack(side = tk.LEFT)

# Close button
close = tk.Button(
    frame,
    text = "Close",
    command = quit
)

# Place the Close button
close.pack(side = tk.LEFT)

root.mainloop()