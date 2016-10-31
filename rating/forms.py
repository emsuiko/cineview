from django import forms
from rating.models import Rating, Contact


class RatingForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(), required=False, label='Kommentar')
    CHOICES = [
                ('0', '0 - keine Angabe'),
                ('1', '1 - sehr gut'),
                ('2', '2 - gut'),
                ('3', '3 - okay'),
                ('4', '4 - schlecht'), ]

    view_2d = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False, initial=0, label='Sicht im 2D-Film')
    view_3d = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False, initial=0, label='Sicht im 3D-Film')

    class Meta:
        model = Rating
        fields = ['view_2d', 'view_3d', 'comment', ]


class CinemaContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'mail', 'city', 'cinema', 'comment', ]
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }


class ContactForm(forms.ModelForm):
    mail = forms.CharField(required=True)
    city = forms.CharField(required=False, label='Stadt')
    cinema = forms.CharField(required=False, label='Kino')
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True, label='Nachricht')

    class Meta:
        model = Contact
        fields = ['name', 'mail', 'city', 'cinema', 'comment', ]