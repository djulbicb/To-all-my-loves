# SMTP - Simple mail transfer protocol
import smtplib

USERNAME = "###"
PASSWORD = "###"

# za svakog providera drugaciji email server
with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
    connection.set_debuglevel(0)
    connection.starttls() # da se pokrene tls security
    connection.login(user=USERNAME, password=PASSWORD)
    # subject:Za naslov
    connection.sendmail(from_addr=USERNAME,
                        to_addrs="###",
                        msg="Subject:Hello\n\nHello Hello")
    connection.close()

# Username and password not accepted. Follow url.
# Gmail doesnt allow smtplib by default
# Manage account > Security > Use phone to sign in OFF
#                           > Two factor authentication OFF
#                           > Less secure app access ON

# On yahoo
# > Account security
# > generate new app password