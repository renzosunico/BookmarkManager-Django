from django.conf.urls import url
from .views import LoginView, LogoutProcess

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutProcess.as_view(), name='logout')
]