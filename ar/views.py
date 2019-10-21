from django.shortcuts import render
from django.http import HttpResponse
from data.models import Why_darsia, Subscriber, User


# Create your views here.
def index(request):
    if request.method != 'POST':
        all_why_darsias = Why_darsia.objects.all()
        context = {
            'all_why_darsias': all_why_darsias,
        }
        return render(request, 'index.html', context)
    else:
        try:
            email = request.POST['email']
        except:
            return HttpResponse("Please try again there is some problem with your request")

        subscriber = Subscriber()
        subscriber.email = email
        subscriber.time_created = str()
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
