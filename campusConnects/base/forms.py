from django import forms
from .models import Event
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['title','image','description','location','start_date','end_date','register_link']
        # widgets = {
        #     'start_date': AdminDateWidget()),
        #     'end_date':  AdminDateWidget()),
        # }

class CreateUserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class PasswordResetForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError('No user with this email address.')
        return email
