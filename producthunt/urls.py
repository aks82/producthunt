from django.contrib import admin
from django.urls import path
from django.conf import settings
import catalog.views
import account.views
from django.conf.urls.static import static
from catalog.models import Product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalog.views.home, name='home'),
    path('signup/', account.views.signup, name='signup'),
    path('login/', account.views.login, name='login'),
    path('signout/', account.views.signout, name='signout'),
    path('product/', catalog.views.create, name='product'),
    path('<int:product_id>/', catalog.views.detail, name='detail'),
    path('<int:product_id>/upvote/', catalog.views.upvote, name='upvote'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
