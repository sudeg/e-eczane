from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "x":"y",
        "num":69,
        "list":[12,34,536,7568,5675,868,5885]
    }
    return render(request, "about.html", my_context)