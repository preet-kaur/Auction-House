from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    # this method is executed when form.is_valid method is called

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        print("sdfhj")
        password = self.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if not user or not user.check_password(password):
            raise forms.ValidationError("Incorrect Details")

        #if
           # raise forms.ValidationError("Password incorrect")

        if not user.is_active:
            raise forms.ValidationError("This user is no longer active")

        return super(LoginForm, self).clean(*args, **kwargs)







        # password = forms.CharField(widget=forms.PasswordInput)

        # class Meta:
        #   model = User
        #  fields = ['username', 'password']
