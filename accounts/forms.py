from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    role = forms.ChoiceField(choices=Profile.USER_ROLES, required=True)
    class Meta:
        model = User
        fields =['username','email','password1','password2']
    
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


# one for user model
# one for the customized profile
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city','phone_number','image','role']

