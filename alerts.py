import smtplib
from email.mime.text import MIMEText

def send_email_alert():
    msg = MIMEText("🔥 ALERT: Fire/Smoke Detected by SmartSafeAI")
    msg["Subject"] = "FIRE ALERT"
    msg["From"] = "your-email@gmail.com"
    msg["To"] = "recipient@gmail.com"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("your-email@gmail.com", "your-app-password")
        server.send_message(msg)

