from django.shortcuts import render

# Create your views here.

def Jinja_Print(request):
    d={'name':'Muni', 'age':23}
    return render(request, 'Jinja_Print.html', context=d)