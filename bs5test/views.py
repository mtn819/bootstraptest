from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "bs5test/index.html")

def about(request):
    return render(request, "bs5test/about.html")