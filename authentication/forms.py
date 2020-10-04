from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=200,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                               label='', help_text="")
    first_name = forms.CharField(max_length=200,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                                 label='')
    last_name = forms.CharField(max_length=200,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
                                label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), label='')
    password1 = forms.CharField(max_length=200,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                                label='')
    password2 = forms.CharField(max_length=200,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
                                label='')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EditProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
