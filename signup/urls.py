from django.conf.urls import url
from .views import SignupView

urlpatterns = [
    url(r'^signup/', SignupView.as_view()),
]