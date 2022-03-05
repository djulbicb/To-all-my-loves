import smtplib

class EmailSender:

    def __init__(self, email:str, password:str):
        self.email = email
        self.password = password

    def sendEmail(self, send_to:str, message:str):
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.set_debuglevel(0)
            connection.starttls()

            connection.login(user=self.email, password=self.password)

            connection.sendmail(from_addr=self.email,
                                to_addrs=send_to,
                                msg=f"Subject:Hello\n\n{message}")
            connection.close()