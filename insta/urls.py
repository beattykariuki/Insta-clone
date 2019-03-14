from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('gram.urls')),
    url(r'^friendship/', include('friendship.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
