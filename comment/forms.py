from django import forms 
from .models import MicroStory

# Model form
class NewStoryForm(forms.ModelForm):
    class Meta():
        model = MicroStory
        fields = ["fullname", "title", "story"]

