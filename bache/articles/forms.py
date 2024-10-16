from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class SendArticleForm(forms.Form):
    title = forms.CharField(min_length=3, max_length=50)
    body = forms.CharField(widget= forms.Textarea)
    published_at = forms.DateField()

    def clean_published_at(self):
        date = self.cleaned_data['published_at']

        if date <= datetime.date.today():
            raise ValidationError(_('The date cannot be in the past. Please enter a valid date.'))

        return date
