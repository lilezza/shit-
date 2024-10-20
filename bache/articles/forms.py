from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Articles , Category

class SendArticleForm(forms.ModelForm):
    # title = forms.CharField(min_length=3, max_length=50)
    # body = forms.CharField(widget= forms.Textarea)
    # published_at = forms.DateField()

    class Meta:
        model = Articles
        fields = ['title','body', 'categories' ,'published_at']
        widgets = {
            'title' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'categories' : forms.SelectMultiple(attrs= {'class' : 'form-control'}),
            'published_at': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

    def clean_published_at(self):
        date = self.cleaned_data['published_at']

        if not self.instance.pk and date < datetime.datetime.today():
            raise ValidationError(_('The date cannot be in the past. Please enter a valid date.'))

        return date
