from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.urls import reverse_lazy

urlpatterns = [
    path('', include('email_app.urls')),
    path('admin/', admin.site.urls),
    path('profile/', user_views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='users/change-password.html', success_url=reverse_lazy('success-password')), name='change-password'),
    path('success-password/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_update.html'), name='success-password'),
]
