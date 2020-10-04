from django.urls import path
from .views import UserRegisterView,UserEditView, PassChangeView, PassChangeSuccessView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view()),
    path('password/',PassChangeView.as_view(), name ='password_change'),
    path('password_change_success/', PassChangeSuccessView, name = 'password_change_success'),
]
