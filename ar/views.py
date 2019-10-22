owner_password = 'MYPASSWORDHAHAHHAH'
owner_email = 'sayedkhalidobaide@gmail.com'

import time
import random
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from data.models import *
from tools.aztool import *


# Create your views here.
def index(request):
    if request.method != 'POST':
        four_reviews = Review.objects.filter(status='On')
        all_why_darsias = Why_darsia.objects.all()
        darsia_logo = Url.objects.get(name='darsia_logo')
        darsia_logo = str(darsia_logo.url)
        darsia_mini_logo = Url.objects.get(name='darsia_mini_logo')
        darsia_mini_logo = str(darsia_mini_logo.url)

        context = {
            'all_why_darsias': all_why_darsias,
            'four_reviews' : four_reviews,
            'darsia_logo' : darsia_logo,
            'darsia_mini_logo' : darsia_mini_logo,
        }
        return render(request, 'index.html', context)

    else:
        try:
            email = request.POST['email']
        except:
            return HttpResponse("Please try again there is some problem with your request")

        subscriber = Subscriber()
        subscriber.email = email
        subscriber.time_created = str(datetime.now())
        subscriber.status = 'On'

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            subscriber.is_user = 'False'
            subscriber.save()
            return HttpResponse('<script>window.location.href="/"</script>')

        subscriber.is_user = 'True'
        subscriber.save()
        return HttpResponse('<script>window.location.href="/"</script>')


def signup(request):
    if request.method != 'POST':

        # The logos
        darsia_logo = Url.objects.get(name='darsia_logo')
        darsia_logo = str(darsia_logo.url)
        darsia_mini_logo = Url.objects.get(name='darsia_mini_logo')
        darsia_mini_logo = str(darsia_mini_logo.url)


        context = {
            'darsia_logo': darsia_logo,
            'darsia_mini_logo' : darsia_mini_logo,
        }
        return render(request, 'pages/signup.html', context)
    else:
        try:
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            re_password = request.POST['re_password']
        except:
            return HttpResponse('<script>window.location.href="/ar/signup"</script>')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            for_send = Timed_User()
            for_send.name = name
            for_send.email = email

            if password != re_password:
                return HttpResponse('<script>window.location.href="/ar/signup"</script>')
            else:
                pass

            for_send.password = password

            all_users = Simple_Data.objects.get(name='all_users')
            all_users.data = str(int(all_users.data) + 1)
            all_users.save()
            sub_email = email[:2].lower()
            for_send.username = sub_email + str(all_users.data)
            for_send.time_created = str(datetime.now())

            # create the code
            rand_number = random.randint(0,200)
            code = str2md5(str(datetime.now()) + str(time.time()) + email + password + str(rand_number))
            for_send.url = code

            for_send.save()

            msg = '''
            Hello And Welcome To Darsia 
            Activate your account using the link below 
            ''' + '127.0.0.1:8000/ar/'+code
            send_mail(owner_email, owner_password, email, 'Darsia Veryfiction Code', msg)

            return HttpResponse('<script>window.location.href="/ar"</script>')

        return HttpResponse('<script>window.location.href="/ar/signup"</script>')


def user(request, userid):
    try:
        user = User.objects.get(id=userid)
    except User.DoesNotExist:
        return HttpResponse('<script>window.location.href="/"</script>')


    # The logos
    darsia_logo = Url.objects.get(name='darsia_logo')
    darsia_logo = str(darsia_logo.url)
    darsia_mini_logo = Url.objects.get(name='darsia_mini_logo')
    darsia_mini_logo = str(darsia_mini_logo.url)


    context = {
        'darsia_logo': darsia_logo,
        'darsia_mini_logo': darsia_mini_logo,
        'user' : user,
    }
    return render(request, 'pages/user.html', context)


def confirm(request, code):
    try:
        timed_user = Timed_User.objects.get(url=code)
    except Timed_User.DoesNotExist:
        return HttpResponse('<script>window.location.href="/ar/signup"</script>')

    for_send = User()

    for_send.name = timed_user.name
    for_send.email = timed_user.email
    for_send.password = timed_user.password
    for_send.username = timed_user.username

    for_send.bio = 'No Bio'
    default_img = 'https://raw.githubusercontent.com/KhalidObaide/Darsia/master/templates/images/download.png'
    for_send.profile_image = default_img

    # other data
    for_send.time_created = str(datetime.now())
    for_send.does_payed = 'False'
    for_send.courses_took = '[]'
    for_send.liked_courses = '[]'
    for_send.paying_times = '[]'
    for_send.total_times_payed = '0'
    for_send.total_payed_money = '0'
    for_send.last_pay_money = '0'
    for_send.first_pay_money = '0'
    for_send.bank_added_time = ''
    for_send.bank_name = ''
    for_send.bank_number = ''
    for_send.bank_cvc = ''
    for_send.bank_date = ''
    for_send.last_charge = ''
    for_send.wallet = '0'
    for_send.save()

    timed_user.delete()

    return HttpResponse('<script>window.location.href="/"</script>')