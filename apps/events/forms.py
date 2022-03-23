from unicodedata import category
from django import forms

class EventForm(forms.Form):
    
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "City eg. Brooklyn",
                "class": "form-control"
            }
        ))
    state = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "State eg. NY",
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
 