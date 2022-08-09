from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder' : 'Enter Password', 'class': 'form-control',}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder' : 'Confirm Password'}))
    class Meta:
        model = Account
        fields = ['first_name','last_name', 'phone_num', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError ('Password Does Not Match.')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your Email'
        self.fields['phone_num'].widget.attrs['placeholder'] = 'Enter your Phone Number'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'