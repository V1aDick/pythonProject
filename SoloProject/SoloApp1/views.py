from django.shortcuts import render

def homePageView(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")
# Create your views here.
