from .models import Main
from django.forms import ModelForm, TextInput, Textarea


class ArduinoForm(ModelForm):
    class Meta:
        model = Main
        fields = ['weather', 'nfc_codes', 'links', 'custom_text']

        widgets = {
            'weather': TextInput(attrs={
                'class': 'form-control bg-dark inputs',
                'placeholder': 'Example sun/cloudy/rain'
            }),
            'nfc_codes': TextInput(attrs={
                'class': 'form-control bg-dark inputs',
                'placeholder': 'name#code, name#code, name#code'
            }),
            'custom_text': TextInput(attrs={
                'class': 'form-control bg-dark inputs',
                'placeholder': 'Example: Good Day!'
            }),
            'links': TextInput(attrs={
                'class': 'form-control bg-dark inputs',
                'placeholder': 'pc1#url,pc2#url'
            })
        }


class ArdCustomtextedit(ModelForm):
    class Meta:
        model = Main
        fields = ['custom_text']

        widgets = {
            'custom_text': TextInput(attrs={
                'class': 'form-control form-control-lg bg-dark',
                'placeholder': 'Example: Good Day!'
            })
        }
