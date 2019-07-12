# Upgrade Market Autosend 1.0.0

import smtplib
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
import csv


def main():
    # Login + email as txt
    s = smtplib.SMTP('SMTP_SERVER')
    s.set_debuglevel(1)
    msg = MIMEText(open('email.txt').read())
    sender = 'SENDER_EMAIL'
    to_sender = 'SENDER_EMAIL'
    passw = 'PASSWORD'
    s.login(sender, passw)

    # Open a CSV file as a list
    f = open('users.csv')
    recipients = []
    csv_f = csv.reader(f)

    for row in csv_f:
        recipients.append(row[0]) 


    msg['Subject'] = "SUBJECT"
    msg['From'] = sender
    msg['To'] = to_sender

    # Magic for sending email as BCC
    s.sendmail(sender, [to_sender] + recipients, msg.as_string()) 


if __name__ == '__main__':
    main()
