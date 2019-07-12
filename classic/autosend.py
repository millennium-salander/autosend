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
    msg = MIMEText("""MAIN_TEXT""")
    sender = 'SENDER_EMAIL'
    to_sender = 'SENDER_EMAIL'
    passw = 'PASSWORD'
    s.login(sender, passw)

    msg['Subject'] = "SUBJECT"
    msg['From'] = sender
    msg['To'] = to_sender

    # Magic for sending email as BCC
    s.sendmail(sender, [to_sender] + recipients, msg.as_string()) 


if __name__ == '__main__':
    main()
