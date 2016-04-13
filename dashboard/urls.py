from django.conf.urls import url
from .views import DashboardIndex

urlpatterns = [
    url(r'^dashboard/', DashboardIndex.as_view(), name='dashboard'),
]