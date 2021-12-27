from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.views.generic.base import (
    TemplateView,
)
from django.views.generic.edit import (
    CreateView,
)
from .forms import CustomUserCreationForm

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('signup/', CreateView.as_view(template_name='accounts/signup.html', form_class=CustomUserCreationForm, success_url=reverse_lazy('accounts:login')), name='signup')
]
