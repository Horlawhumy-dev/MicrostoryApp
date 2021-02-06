from django.shortcuts import render
from comment.models import MicroStory


# Create your views here.

def results_view(request):
    posts = MicroStory.objects.all().order_by('date_time')
    context = {'posts': posts}
    return render(request, 'results_app/results.html', context)
