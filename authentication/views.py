from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, UserChangeForm


def PassChangeSuccessView(request):
    return render(request, 'registration/password_change_success.html', {})


class PassChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_change_success')


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):  # Profile Information of the current user
        return self.request.user
