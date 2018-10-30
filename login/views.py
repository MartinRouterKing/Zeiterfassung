from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response


# Create your views here.
def login(request):
    form = AuthenticationForm(request)
    return render_to_response("registration/login.html", {
        'form':form
    })
