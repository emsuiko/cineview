from django import forms
from rating.models import Rating


class RatingForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea())
    CHOICES = [
                ('1', '1 - sehr gut'),
                ('2', '2 - gut'),
                ('3', '3 - okay'),
                ('4', '4 - schlecht'), ]

    view_2d = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    view_3d = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Rating
        fields = ['view_2d', 'view_3d', 'comment', ]
