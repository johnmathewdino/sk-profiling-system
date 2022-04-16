from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from django.forms import DateInput


from .models import Profile

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password'].label = ""


    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'Username', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input100',
            'placeholder': 'Password',
            'id': 'hi',
        }
    ))

class profile_form(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name',
                  'middle_name',
                  'last_name',
                  'birthday',
                  'age',
                  'sex',
                  'purok',
                  'education_level',
                  'education_year',
                  'school']
        labels = {
            "first_name": "",
             'middle_name': "",
             'last_name': "",
             'birthday': "",
             'age': "",
             'sex': "",
             'purok': "",
             'education_level': "",
             'education_year': "",
             'school': ""}
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'})
        }

    # def clean(self):
    #     super(profile_form, self).clean()
    #     first_name = self.cleaned_data['first_name']
    #     last_name = self.cleaned_data['last_name']
    #     if self.cleaned_data['middle_name'] != "":
    #         middle_name = self.cleaned_data['middle_name']
    #         if Profile.objects.filter(first_name=first_name, middle_name=middle_name,last_name=last_name).exists():
    #             raise forms.ValidationError(f'"{first_name, middle_name, last_name}" already exists')
    #         return first_name
    #     else:
    #         if Profile.objects.filter(first_name=first_name, last_name=last_name).exists():
    #             raise forms.ValidationError(f'"{first_name,last_name}" already exists')
    #         return first_name