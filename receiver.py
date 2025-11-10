import poplib, time
from email.parser import BytesParser
from datetime import datetime

USERNAME = "amitoujacodes@gmail.com"
APP_PASS = "zlyctvtehuodtias"

last_count = 0
print("📩 Starting receiver (poll every 5s). Ctrl+C to stop.\n")

while True:
    try:
        with poplib.POP3_SSL("pop.gmail.com", 995, timeout=10) as mail:
            mail.user(USERNAME)
            mail.pass_(APP_PASS)
            resp, items, _ = mail.list()
            count = len(items)
            if count > last_count:
                print(f"\n[{datetime.now()}] ✉️ New email received ({count - last_count} new)")
                resp, lines, _ = mail.retr(count)
                raw = b"\n".join(lines)
                msg = BytesParser().parsebytes(raw)
                print("From:", msg.get("From"))
                print("Subject:", msg.get("Subject"))
                print("Body:", msg.get_payload(decode=True).decode(errors="ignore"))
            last_count = count
    except Exception as e:
        print("POP3 error:", e)
    time.sleep(5)
