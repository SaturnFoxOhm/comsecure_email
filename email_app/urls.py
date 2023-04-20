from django.urls import path
from .views import (
    SentMailListView,
    ReceivedMailListView,
    SecretMailListView,
    MailDetailView,
    MailCreateView,
    PasscodeDetailView,
)


urlpatterns = [
    path('', ReceivedMailListView.as_view(), name='email-home'),
    path('sent/', SentMailListView.as_view(), name='email-sent'),
    path('mail/<int:pk>/', MailDetailView.as_view(), name='email-detail'),
    path('compose/', MailCreateView.as_view(), name='email-form'),
    path('secret/', SecretMailListView.as_view(), name='email-secret'),
    path('secret/<int:pk>/', PasscodeDetailView.as_view(), name='email-secret-passcode'),
]
