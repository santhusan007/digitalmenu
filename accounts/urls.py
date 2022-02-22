from django.urls import path
from .views import signup_view,login_view
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login', login_view, name="login"),
    path('signup', signup_view, name="signup"),
    #path('logout',logout_view, name="logout"),
    path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
]
