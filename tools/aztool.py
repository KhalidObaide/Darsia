import hashlib
import smtplib

# md5 function
def str2md5(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


# email sending
def send_mail(owner_email, owner_password, to, sub, msg):
    web = owner_email
    web_password = owner_password
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(web, web_password)
    message = f"Subject: {sub}\n\n{msg}"
    server.sendmail(web, to, message)
    server.quit()

