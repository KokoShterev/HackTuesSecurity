import pyotp

import smtplib
import ssl
from email.message import EmailMessage

key ="neshtorandom"
counter = 0
hotp = pyotp.HOTP(key)

print("please enter your email")
email = input()
email_sender = 'fdjkhghdfjkg@gmail.com'
email_password ='vwfkejkyxvgyshuq'
email_receiver = email

subject = "We want to reward you for your service "
body ="""your otp is  """ + hotp.at(0)

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com" , 465 , context=context ) as smtp:
    smtp.login(email_sender , email_password)
    smtp.sendmail(email_sender , email_receiver, em.as_string())
for _ in range(1):
    print(hotp.verify(input("Enter Code:" ), counter))
    counter += 1
