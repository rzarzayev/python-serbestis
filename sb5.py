import smtplib
from email.mime.text import MIMEText

def send_alert_email(ip, port):
    sender = "your_email@example.com"
    receiver = "alert_recipient@example.com"
    subject = "Yeni hücum aşkar edildi!"
    body = f"Hücum IP: {ip}, Port: {port}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login("your_email@example.com", "your_password")
            server.sendmail(sender, receiver, msg.as_string())
            print("E-poçt xəbərdarlığı göndərildi.")
    except Exception as e:
        print(f"E-poçt göndərilərkən xəta baş verdi: {e}")

# Nümunə çağırış
send_alert_email("192.168.1.10", 8080)
