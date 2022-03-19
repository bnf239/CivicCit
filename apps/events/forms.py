from unicodedata import category
from django import forms

class EventForm(forms.Form):
    
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Location",
                "class": "form-control"
            }
        ))

    category = forms.ChoiceField(
                    
                    required = True,
                    label='Category',
                    widget=forms.Select(attrs={'class': 'form-control'}),
                     choices=(
    ("community--events", "Community"),
    ("family-and-education--events", "Family & Education"),
    ("charity-and-causes--events", "Charity & Causes"),
    ("government--events", "Government & Politics"),
    ("science-and-tech--events", "Science & Tech"),
))
 