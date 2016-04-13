from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model
User = get_user_model()

class SignupView(FormView):

    model = User
    template_name = 'signup/signup.html'
    form_class = UserRegistrationForm

    def post(self, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form

        if form.is_valid():
            form.save()
            return redirect('login:login')

        return self.render_to_response(context)
