from django.shortcuts import redirect, render


# Create your views here.

def index_view(request):
    return render(request,"index.html")