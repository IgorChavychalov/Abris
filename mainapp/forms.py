from authapp.models import User
from django import forms

from .models import Draw


class NewDrawForm(forms.ModelForm):
    class Meta:
        model = Draw
        fields = ('name', 'forestry', 'quarter', 'letter')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

