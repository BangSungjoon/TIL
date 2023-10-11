from django import forms

# forms.Form 상속
class DataForm(forms.Form):
    name = forms.CharField(max_length=10,
                           label='이름2')
    
    age = forms.IntegerField(label='나이2')