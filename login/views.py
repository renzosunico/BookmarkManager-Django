from .forms import LoginForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from django.views.generic.edit import FormView
from django.views.generic import View

from django.contrib.auth import get_user_model, login, authenticate, logout
User = get_user_model()

from braces.views import AnonymousRequiredMixin


class LoginView(AnonymousRequiredMixin, FormView):

    model = User
    template_name = 'login/login.html'
    form_class = LoginForm
    authenticated_redirect_url = 'dashboard:dashboard'

    def form_valid(self, form):
        login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return redirect('dashboard:dashboard')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def post(self):
        if self.request.user.is_authenticated():
            redirect()


class LogoutProcess(View):

    def get(self, request, *args, **kwargs):
        logout(self.request)
        return redirect('action:login')