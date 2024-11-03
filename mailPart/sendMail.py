
import smtplib
from email.message import EmailMessage
import sys
import os
from dotenv import load_dotenv


load_dotenv()

# Set the sender email and password and recipient email
from_email_addr = os.environ.get("from_email_addr")
from_email_pass = os.environ.get("from_email_pass")
to_email_addr = os.environ.get("to_email_addr")
ip = sys.argv[1]

# Create a message object
msg = EmailMessage()

# Set the email body
body =f'current ip {ip}'
msg.set_content(body)

# Set sender and recipient
msg['From'] = from_email_addr
msg['To'] = to_email_addr

# Set your email subject
msg['Subject'] = f'[Raspberry] Ip {ip}'

# Connecting to server and sending email
# Edit the following line with your provider's SMTP server details
server = smtplib.SMTP('smtp.gmail.com', 587)

# Comment out the next line if your email provider doesn't use TLS
server.starttls()
# Login to the SMTP server
server.login(from_email_addr, from_email_pass)

# Send the message
server.send_message(msg)

print('Email sent')

#Disconnect from the Server
server.quit()