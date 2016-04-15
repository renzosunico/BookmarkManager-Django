from django.conf.urls import url
from .views import DashboardIndex, DeleteBookmark, EditBookmark

urlpatterns = [
    url(r'^dashboard/', DashboardIndex.as_view(), name='dashboard'),
    url(r'^delete_bookmark/(?P<pk>\d+)/', DeleteBookmark.as_view(), name='delete-bookmark'),
    url(r'^edit_bookmark/(?P<pk>[0-9]+)', EditBookmark.as_view(), name='edit-bookmark'),
]