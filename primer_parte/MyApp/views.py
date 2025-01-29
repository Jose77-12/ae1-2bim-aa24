from django.shortcuts import render # type: ignore

# Create your views here.
def listPlatosTipicos(request):
    return render(request, 'listPlatosTipicos.html')