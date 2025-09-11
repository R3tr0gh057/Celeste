import smtplib
from core.config import get_email_credentials

def send_email(to, content):
    email, password = get_email_credentials()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    server.sendmail(email, to, content)
    server.close()
    return "Email sent."
