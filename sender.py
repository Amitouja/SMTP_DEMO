# sender.py
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

SENDER = "amitoujacodes@gmail.com"
APP_PASS = "zlyctvtehuodtias"   # <- paste the 16-char App Password here
RECEIVER = "amitoujacodes@gmail.com"  # you can send to yourself

msg = MIMEText("Hi,I'm Amitouja Tagore and I am glad you received the Realtime SMTP test sent at " + datetime.now().isoformat())
msg["Subject"] = "Realtime SMTP Demo from Amitouja!"
msg["From"] = SENDER
msg["To"] = RECEIVER

with smtplib.SMTP("smtp.gmail.com", 587) as s:
    s.ehlo()
    s.starttls()
    s.login(SENDER, APP_PASS)
    s.send_message(msg)
    print("Sent at", datetime.now())
