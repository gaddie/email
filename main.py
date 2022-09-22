from email.message import EmailMessage
import smtplib
import ssl

email_sender = "dailydeals9396@gmail.com"
email_receiver = "gadsonmulonga@gmail.com"
email_password = "byxbqcsrmwkulknk"

subject = "Daily Deals"
body = "This is a test email"

em = EmailMessage()
em["Subject"] = subject
em["From"] = email_sender
em["To"] = email_receiver
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, em.as_string())
    