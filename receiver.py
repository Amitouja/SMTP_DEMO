# receiver.py
import poplib, time
from email.parser import BytesParser
from datetime import datetime

USERNAME = "amitoujacodes@gmail.com"
APP_PASS = "zlyctvtehuodtias"  # same app password

def fetch_latest():
    try:
        mail = poplib.POP3_SSL("pop.gmail.com", 995, timeout=10)
        mail.user(USERNAME)
        mail.pass_(APP_PASS)
        resp, items, octets = mail.list()
        count = len(items)
        if count == 0:
            print(f"[{datetime.now()}] Inbox empty")
        else:
            resp, lines, octets = mail.retr(count)  # fetch latest message
            raw = b"\n".join(lines)
            msg = BytesParser().parsebytes(raw)
            print(f"\n[{datetime.now()}] New mail:")
            print("From:", msg.get("From"))
            print("Subject:", msg.get("Subject"))
            print("Body:", msg.get_payload())
        mail.quit()
    except Exception as e:
        print("POP3 error:", e)

print("Starting receiver (poll every 5s). Ctrl+C to stop.")
while True:
    fetch_latest()
    time.sleep(5)
