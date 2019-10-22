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


def str2arr(array):
    returnner = []
    new_array = array
    new_array = new_array.replace(']', '')
    new_array = new_array.replace('[', '')
    while True:
        is_kame = ',' in new_array
        if is_kame:
            kame_place = int(new_array.index(','))
            pass
        else:
            break
        kame_word = new_array[0: kame_place:]
        returnner.append(kame_word)
        kame_word = new_array[0: kame_place + 1:]
        new_array = new_array.replace(kame_word, '')
    return returnner

