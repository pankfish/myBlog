from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})
def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def contact_view(request, *args, **kwargs):
    form = ContactForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
    return render(request, "contact.html", context)

def blog_view(request, *args, **kwargs):
    post = {
        "Title": "Trash In Space?",
        "Author": "Matty Ice",
        "Content": "Step 1: rent a warehouse, Step 2: Fill it with cans ...... Step 5: profit"
    }
    return render(request, "blog.html", post)
