from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('signup.urls', namespace='signup')),
    url(r'', include('login.urls', namespace='action')),
    url(r'', include('dashboard.urls', namespace='dashboard')),
]
