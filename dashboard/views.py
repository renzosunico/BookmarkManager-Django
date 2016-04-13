from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from braces.views import LoginRequiredMixin

from django.views.generic import TemplateView


class DashboardIndex(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'
    login_url = 'login:login'
    raise_exception = False
