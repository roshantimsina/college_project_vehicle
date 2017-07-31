# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .decorators import check_recaptcha
from .forms import SignUpForm



# @check_recaptcha

# signup views
class UserSignupForm(View):
    form_class = SignUpForm
    template_name = 'signup.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns these objects if credential are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #after signup redirect to profile settings
                    return redirect('profile')
                    
        return render(request, self.template_name, {'form':form})
