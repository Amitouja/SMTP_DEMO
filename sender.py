import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime

SENDER = "amitoujacodes@gmail.com"
APP_PASS = "zlyctvtehuodtias"
RECEIVER = "amitoujaboset@gmail.com"

timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')

# --- Plain text fallback ---
text_content = f"""\
Hi there,

This is Amitouja Tagore, and I'm glad you received the Realtime SMTP demo email!

✅ Sent on: {timestamp}
✅ Status: Successfully Delivered

Thanks for testing Realtime SMTP delivery!

Best regards,
Amitouja Tagore
"""

# --- HTML body with embedded signature image ---
html_content = f"""\
<!DOCTYPE html>
<html>
  <body style="font-family: Arial, sans-serif; background-color: #f7f8fa; padding: 0; margin: 0;">
    <div style="max-width: 600px; margin: auto; background: #ffffff; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); overflow: hidden;">
      <div style="padding: 20px;">
        <h2 style="color: #2563eb;">Realtime SMTP Demo – Delivery Confirmation</h2>
        <p>Hi there,</p>
        <p>This is <strong>Amitouja Tagore</strong>, and I'm happy to confirm that your Realtime SMTP test email was sent successfully!</p>
        <ul>
          <li><strong>Sent on:</strong> {timestamp}</li>
          <li><strong>Status:</strong> Delivered Successfully</li>
        </ul>
        <p>Thank you for trying out the Realtime SMTP demo!</p>

        <!-- Inline signature section -->
        <hr style="margin-top: 30px; border: none; border-top: 1px solid #ddd;" />
        <div style="margin-top: 15px;">
          <p style="font-size: 14px; color: #555;">
            Best regards,<br>
            <strong style="color: #2563eb;">Amitouja Tagore</strong><br>
            <span style="color: #777;">Developer | Network Enthusiast</span><br>
            <a href="mailto:amitoujacodes@gmail.com" style="color: #2563eb; text-decoration: none;">amitoujacodes@gmail.com</a><br>
            <span style="font-size: 12px; color: #999;">Sent via Python SMTP Automation</span><br><br>
            <img src="cid:signature" alt="Signature" style="width: 180px; height: auto; border-radius: 5px;">
          </p>
        </div>
      </div>
    </div>
  </body>
</html>
"""

# --- Create email ---
msg = MIMEMultipart("related")
msg["Subject"] = "Realtime SMTP Demo – Delivery Confirmation"
msg["From"] = SENDER
msg["To"] = RECEIVER

alt_part = MIMEMultipart("alternative")
alt_part.attach(MIMEText(text_content, "plain"))
alt_part.attach(MIMEText(html_content, "html"))
msg.attach(alt_part)

# --- Attach inline image ---
with open("signature.png", "rb") as f:
    img = MIMEImage(f.read())
    img.add_header("Content-ID", "<signature>")
    img.add_header("Content-Disposition", "inline", filename="signature.png")
    msg.attach(img)

# --- Send email ---
with smtplib.SMTP("smtp.gmail.com", 587) as s:
    s.starttls()
    s.login(SENDER, APP_PASS)
    s.send_message(msg)
    print("✅ Email with inline PNG signature sent at", timestamp)
