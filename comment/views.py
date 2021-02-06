from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from .models import MicroStory
from .forms import NewStoryForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='register:signin')
def comment_view(request):
    if request.method == "POST":
        # initiating the model form
        form = NewStoryForm(request.POST)
        # getting user values
        name = request.POST.get('fullname')
        storytitle = request.POST.get('title')
        story = request.POST.get('story')
        # if sometging actuall passed into it the inputs
        if form.is_valid():
            # instantitaing the user object
            newstory = MicroStory(fullname=name, title=storytitle, story=story)
            # saving to the django admin database
            newstory.save()
            messages.success(request, 'Your story got posted successfully!')
            # redirecting  if successful posted
            return redirect('/results')
    # return 'results_app/results.html'
    return render(request, 'comment/comment.html')