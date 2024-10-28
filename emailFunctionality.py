# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import ssl
# # Email credentials
# yahoo_user = "creamykeylogger@yahoo.com"
# yahoo_password = "Ihatethisuni2004"

# # Email details
# to_email = "creamykeylogger@yahoo.com"
# subject = "Test Email from Python (Yahoo SMTP with SSL)"
# body = "Hello! This is a test email sent from Python using Yahoo SMTP with SSL."

# # Create the email
# msg = MIMEMultipart()
# msg['From'] = yahoo_user
# msg['To'] = to_email
# msg['Subject'] = subject
# msg.attach(MIMEText(body, 'plain'))

# try:

#     # context = ssl._create_unverified_context()
#     print ("start")
#     server = smtplib.SMTP("smtp.mail.yahoo.com", 587, timeout=10)
#     server.starttls()
#     server.login(yahoo_user, yahoo_password)
#     print ("end")
    
#     server.sendmail(yahoo_user, to_email, msg.as_string())
#     server.quit()

#     print('Email sent successfully!')
# except Exception as e:
#     print(f'Failed to send email: {e}')

# from here
# import smtplib
# from email.mime.text import MIMEText
# SMTP_SERVER = "smtp.mail.yahoo.com"
# SMTP_PORT = 587


# SMTP_USERNAME = "creamykeylogger@yahoo.com"
# SMTP_PASSWORD = "Ihatethisuni2004"
# EMAIL_FROM = "creamykeylogger@yahoo.com"
# EMAIL_TO = "creamykeylogger@yahoo.com"
# EMAIL_SUBJECT = "REMINDER:"
# co_msg = """
# Hello
# """
# def send_email():
#     msg = MIMEText(co_msg)
#     msg['Subject'] = EMAIL_SUBJECT + "Company - Service at appointmentTime"
#     msg['From'] = EMAIL_FROM 
#     msg['To'] = EMAIL_TO
#     debuglevel = True
#     mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#     mail.set_debuglevel(debuglevel)
#     mail.starttls()
#     mail.login(SMTP_USERNAME, SMTP_PASSWORD)
#     mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
#     mail.quit()

# if __name__=='__main__':
#     send_email()

# new stuff gmail

# import smtplib
# from email.mime.text import MIMEText

# subject = "covidtimes2020"
# body = "This is the body of the text message"
# sender = "info.spearbank@gmail.com"
# recipients = ["info.spearbank@gmail.com", "info.spearbank@gmail.com"]
# password = "covidtimes2020"


# def send_email(subject, body, sender, recipients, password):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = ', '.join(recipients)
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
#        smtp_server.login(sender, password)
#        smtp_server.sendmail(sender, recipients, msg.as_string())
#     print("Message sent!")


# send_email(subject, body, sender, recipients, password)

# import sendgrid
# import os
# from sendgrid.helpers.mail import Mail, Email, To, Content

# my_sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

# # Change to your verified sender
# from_email = Email("creamykeylogger@yahoo.com")  

# # Change to your recipient
# to_email = To("creamykeylogger@yahoo.com")  

# subject = "Lorem ipsum dolor sit amet"
# content = Content("text/plain", "consectetur adipiscing elit")

# mail = Mail(from_email, to_email, subject, content)

# # Get a JSON-ready representation of the Mail object
# mail_json = mail.get()

# # Send an HTTP POST request to /mail/send
# response = my_sg.client.mail.send.post(request_body=mail_json)

### new new new

# import os
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders


# # Set up email details from environment variables
# sender_email = "MS_wq2PZ2@trial-vywj2lpmokql7oqz.mlsender.net"
# password = "poPAl1rUvEnwgGEW"
# smtp_server = "smtp.mailersend.net"
# smtp_port = "587"

# # Define the receiver email
# receiver_email = "rashu.kharbanda@gmail.com"

# subject = "Welcome to Amazing Company"
# body = """
# Hey there!

# Thanks for joining us at Amazing Company. Your email has been verified and your account has been created.
# Head to the website to login and start using our features."""

# # Create the email message
# message = MIMEMultipart()
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Subject"] = subject

# # Attach the email body to the message
# message.attach(MIMEText(body, "plain"))

# # Establish a connection to the SMTP server and send the email
# try:
#     # Connect to the SMTP server
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls()  # Secure the connection
#         server.login(sender_email, password)  # Log in to the SMTP server
#         server.sendmail(
#             sender_email, receiver_email, message.as_string()
#         )  # Send the email
#     print("Email sent successfully")
# except Exception as e:
#     print(f"Error: {e}")

##### new new 44

# from mailersend import emails
# import os


# # Initialize the MailerSend email client with the API key
# mailer = emails.NewEmail("mlsn.524b32ecd5a2dcda34d6ed34e96520b01aaed50da331a359f44116fbe0f40de6")

# # Define an empty dict to populate with mail values
# mail_body = {}

# # Define the sender email details
# mail_from = {
#     "name": "Amazing Company",
#     "email": "hello@amazingcompany.com",
# }

# # Define the recipient email details
# recipients = [
#     {
#         "name": "Rashu",
#         "email": "rashu.kharbanda@gmail.com",
#     }
# ]

# # Define the reply-to email details
# reply_to = {
#     "name": "Customer Support Replies",
#     "email": "reply@amazingcompany.com",
# }

# # Set the sender email details
# mailer.set_mail_from(mail_from["email"], mail_body)

# # Set the recipient email details
# mailer.set_mail_to(recipients, mail_body)

# # Set the subject of the email
# mailer.set_subject("Your account has been created!", mail_body)

# # Set the HTML content of the email
# mailer.set_html_content(
#     "<h1>Welcome to Amazing Company!</h1> "
#     "<p>Thanks for joining us, we’re so happy to have you. Your account is ready to go.</p>"
#     "<p>To get started, login to your dashboard and head to your profile.</p>"
#     "<p>Best regards, The Amazing Company Team</p>",
#     mail_body,
# )

# # Set the plain text content of the email
# mailer.set_plaintext_content(
#     "Welcome to Amazing Company! Thanks for joining us, we’re so happy to have you. "
#     "Your account is ready to go. To get started, login to your dashboard and head to your profile. "
#     "Best regards, The Amazing Company Team",
#     mail_body,
# )

# # Set the reply-to email details
# mailer.set_reply_to(reply_to["email"], mail_body)

# # Send the email and print the response (status code and data)
# try:
#     response = mailer.send(mail_body)
#     print("Status Code:", response.status_code)
#     print("Response JSON:", response.json())
# except Exception as e:
#     print(f"An error occurred: {e}")

###### try 6

# # the first step is always the same: import all necessary components:
# import smtplib
# from socket import gaierror

# # now you can play with your code. Let’s define the SMTP server separately here:

# port = 587 
# smtp_server = "live.smtp.mailtrap.io"
# login = "api" # paste your login generated by Mailtrap
# password = "c2151af737bd447f8f82331e58edbda8" # paste your password generated by Mailtrap
# # specify the sender’s and receiver’s email addresses
# sender = "hello@demomailtrap.com"
# receiver = "ukharbanda20@gmail.com"

# # type your message: use two newlines (\n) to separate the subject from the message body
# # and use 'f' to  automatically insert variables in the text
# message = f"""\
# Subject: Hi Mailtrap
# To: {receiver}
# From: {sender}
# This is my first message with Python."""

# try:
#     #send your message with credentials specified above
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.login(login, password)
#         server.sendmail(sender, receiver, message)
#     # tell the script to report if your message was sent or which errors need to be fixed 
#     print('Sent')
# except (gaierror, ConnectionRefusedError):
#     print('Failed to connect to the server. Bad connection settings?')
# except smtplib.SMTPServerDisconnected:
#     print('Failed to connect to the server. Wrong user/password?')
# except smtplib.SMTPException as e:
#     print('SMTP error occurred: ' + str(e))

#### test 7

import smtplib

sender = "Private Person <hello@demomailtrap.com>"
receiver = "A Test User <ukharbanda20@gmail.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
    server.starttls()
    server.login("api", "c2151af737bd447f8f82331e58edbda8")
    server.sendmail(sender, receiver, message)