# import csv
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mail_send(subject,sender_email,password,receiver_email,message):

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    # text =message
    html = """
    CBFBDSNDNDN
"""

    # Turn these into plain/html MIMEText objects
    # part1 = MIMEText(text.as_string(), "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    # message.attach(part1)
    message.attach(part2)

    # server.login(sender_email, password)
    with smtplib.SMTP("mail.tikuntech.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())


import csv


# with open("output_info.csv", 'r',encoding="utf-8") as file:
#   csvreader = csv.reader(file)
# #   next()
#   for row in csvreader:
#     # print(row)
# try:
#         sender_email = "datamanagement@tikuntech.com"
#         receiver_email = ["dlovej009@gmail.com"]
#         password = "Maidenatlanta123"
#         # message=""
#         print("Done")
#         subject="Tikuntech"
#         message = """\

#         This is my first email sent through Python smtplib."""
#         mail_send(subject,sender_email,password,receiver_email,message)
# except Exception as err:
#         print(err)
#         pass
        
