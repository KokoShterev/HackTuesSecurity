import pyotp

import smtplib
import ssl
from email.message import EmailMessage


def two_factor_authentication(email):
    key = "neshtorandom"
    counter = 0
    hotp = pyotp.HOTP(key)
    email_sender = 'fdjkhghdfjkg@gmail.com'
    email_password = 'vwfkejkyxvgyshuq'
    email_receiver = email

    subject = "Two Factor Authentication"
    body = """your otp is  """ + hotp.at(0)

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    return em.as_string()
