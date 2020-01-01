# Upgrade Market Autosend 1.1.0

import smtplib
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
import csv


def main():
    # Login + email as txt
    s = smtplib.SMTP('SMTP_SERVER')
    s.set_debuglevel(1)
    msg = EmailMessage()
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

    msg.set_content("""\
    Salut!

    Cela ressemble à un excellent recipie[1] déjeuner.

    [1] http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718

    --Pepé
    """)

    # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.
    asparagus_cid = make_msgid()
    msg.add_alternative("""\
    <html>
      <head></head>
      <body>
        <p>Salut!</p>
        <p>Cela ressemble à un excellent
            <a href="http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718>
                recipie
            </a> déjeuner.
        </p>
        <img src="cid:{asparagus_cid}" />
      </body>
    </html>
    """.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')
    # note that we needed to peel the <> off the msgid for use in the html.

    # Now add the related image to the html part.
    with open("roasted-asparagus.jpg", 'rb') as img:
        msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                         cid=asparagus_cid)


    # Magic for sending email as BCC
    s.sendmail(sender, [to_sender] + recipients, msg.as_string()) 


if __name__ == '__main__':
    main()
