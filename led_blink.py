from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# defining the pin of Raspberry Pi
RedLED = 11
BlueLED = 13
GreenLED = 15

GPIO.setup(RedLED, GPIO.OUT)
GPIO.setup(BlueLED, GPIO.OUT)
GPIO.setup(GreenLED, GPIO.OUT)

#turning all the LED off initially
GPIO.output(RedLED, GPIO.LOW)
GPIO.output(BlueLED, GPIO.LOW)
GPIO.output(GreenLED, GPIO.LOW)

# creating window
win = Tk()
win.title("LED Toggle")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

#event functions
def ToggleRedLED():
    if GPIO.input(11)==1:
        GPIO.output(RedLED, GPIO.LOW)
        RedLEDButton["text"] = "Turn RedLED led on"
    else:
        GPIO.output(RedLED, GPIO.HIGH)
        RedLEDButton["text"] = "Turn RedLED led off"
def ToggleBlueLED():
    if GPIO.input(13)==1:
        GPIO.output(BlueLED, GPIO.LOW)
        BlueLEDButton["text"] = "Turn BlueLED led on"
    else:
        GPIO.output(BlueLED, GPIO.HIGH)
        BlueLEDButton["text"] = "Turn BlueLED led off"
def ToggleGreenLED():
    if GPIO.input(15)==1:
        GPIO.output(GreenLED, GPIO.LOW)
        GreenLEDButton["text"] = "Turn GreenLED led on"
    else:
        GPIO.output(GreenLED, GPIO.HIGH)
        GreenLEDButton["text"] = "Turn GreenLED led off"

# function to close the window and turn all LED off
def close():
    GPIO.cleanup()
    win.destroy()

# creating widgets/buttons
RedLEDButton = Button(win, text = 'Turn RedLEDLed on', font = myFont, command = ToggleRedLED, bg='bisque2', height = 1, width = 24)
RedLEDButton.grid(row=0,column=1)
BlueLEDButton = Button(win, text = 'Turn BlueLed on', font = myFont, command = ToggleBlueLED, bg='bisque2', height = 1, width = 24)
BlueLEDButton.grid(row=1,column=1)
GreenLEDButton = Button(win, text = 'Turn GreenLed on', font = myFont, command = ToggleGreenLED, bg='bisque2', height = 1, width = 24)
GreenLEDButton.grid(row=2,column=1)

exitButton = Button(win, text = 'exit', font = myFont, command = close, bg='RedLED', height = 1, width = 6)
exitButton.grid(row=3,column=1)

#exit with the close button on the top right of the window
win.protocol("WN_DELETE_WINDOW", close)

#loop
win.mainloop()