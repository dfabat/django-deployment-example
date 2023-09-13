from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

# criando uma nova classe para formulários que será vinculada ao banco de dados
class UserForm(forms.ModelForm):

    # password
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ("portfolio_site", "profile_pic")