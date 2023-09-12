from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

# Initializing GPIO
GPIO.setmode(GPIO.BCM)

# HARDWARE #
led_red = LED(13)
led_green = LED(23)
led_blue = LED(26)

# GUI DEFINITION is here #
win = Tk()
win.title("LED Controller")
myFont = tkinter.font.Font(family="Arial", size=23, weight="normal")

# EVENT FUNCTIONS #

# The ability to change the button wording and the LED's state

def ledToggle(led, button):
    if led.is_lit:
        led.off()
        button["text"] = f"Turn {button['text'].split()[1]} On"
    else:
        led.on()
        button["text"] = f"Turn {button['text'].split()[1]} Off"

# Close the application after clearing the GPIO.

def exitFunction():
    GPIO.cleanup()
    win.destroy()

# WIDGETS #
# Control button for the Red LED

button_Red = Button(win, text="Turn Red Off", font=myFont, command=lambda: ledToggle(led_red, button_Red), bg='red', height=6, width=21)
button_Red.grid(row=0, column=0)

# Control button for the Green LED

button_Green = Button(win, text="Turn Green Off", font=myFont, command=lambda: ledToggle(led_green, button_Green), bg='green', height=6, width=21)
button_Green.grid(row=0, column=1)

# Control button for the Blue LED

button_Blue = Button(win, text="Turn Blue Off", font=myFont, command=lambda: ledToggle(led_blue, button_Blue), bg='blue', height=6, width=21)
button_Blue.grid(row=0, column=2)

# Exit the application button

exitButton = Button(win, text="Exit", font=myFont, command=exitFunction, bg="blue", height=4, width=23)
exitButton.grid(row=1, column=1)
# Launch the main GUI loop.
win.mainloop()
