from django.shortcuts import render
from data.models import Why_darsia


# Create your views here.
def index(request):
    all_why_darsias = Why_darsia.objects.all()
    context = {
        'all_why_darsias' : all_why_darsias,
    }
    return render(request, 'index.html', context)
