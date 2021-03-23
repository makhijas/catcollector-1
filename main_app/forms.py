from django import forms
from .models import Feeding

class FeedingForm(forms.ModelForm):
    # meta class because that's how django does it
    class Meta: 
        # specify the model:
        model = Feeding
        fields = ['date', 'meal']

