from django.urls import path
from django.contrib.auth.views import (
    LoginView,
)
from django.views.generic.base import (
    TemplateView,
)

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
]
