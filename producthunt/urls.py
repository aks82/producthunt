from django.contrib import admin
from django.urls import path
import catalog.views
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalog.views.home, name='home'),
    path('signup/', account.views.signup, name='signup'),
    path('login/', account.views.login, name='login'),
    path('signout/', account.views.signout, name='signout'),
]
