from django import forms
from django.forms import ModelForm
from .models import Data
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = ['tenure', 'seniorCitizen', 'partner', 
        'dependents', 'phone_service', 'internet_service', 'charges','contract', 'payment_method']


        # labels = {
        #     'gender':'',
        #     'tenure':'',
        #     'seniorCitizen':'',
        #     'partner':'',
        #     'dependents':'',
        #     'phone_service':'',
        #     'internet_service':'',
        #     'charges':'',
        #     'payment_method':'',
        # }
        # widgets = {
        #     'gender': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter gender'}),
        #     'tenure':forms.TextInput(attrs={'placeholder':'Enter tenure'}),
        #     'seniorCitizen':'',
        #     'partner':'',
        #     'dependents':'',
        #     'phone_service':'',
        #     'internet_service':'',
        #     'charges':'',
        #     'payment_method':'',
        # }

    def __init__(self, *args, **kwargs):
        super(DataForm, self).__init__(*args, **kwargs)
        self.fields['tenure'].empty_label = 'Select tenure'
        self.fields['seniorCitizen'].empty_label = 'Select'
        self.fields['partner'].empty_label = 'Select partner'
        self.fields['dependents'].empty_label = 'Select dependents'
        self.fields['phone_service'].empty_label = 'Select phone service'
        self.fields['internet_service'].empty_label = 'Select internet service'
        self.fields['charges'].empty_label = 'Select charges'
        self.fields['contract'].empty_label = 'Select contract'
        self.fields['payment_method'].empty_label = 'Select payment method'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

        labels = {
            # 'email': '',
            # 'username': '',
            # 'password1': '',
            # 'password2': '',
        }

        widgets = {
            'email' : forms.TextInput(attrs={'placeholder':'abc@gmail.com'}),
            'username' : forms.TextInput(attrs={'placeholder':'kaki'}),
            'password1' : forms.TextInput(attrs={'placeholder':'create password'}),
            'password2' : forms.TextInput(attrs={'placeholder':'confirm password'}),
        }
