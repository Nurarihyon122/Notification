import smtplib
def send_email(to, message):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your-email@gmail.com', 'password')
        server.sendmail('your-email@gmail.com', to, message)
