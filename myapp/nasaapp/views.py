from django.shortcuts import render

def index(request):
    context = {
        'title': 'My Nasa App',
    }
    return render(request, 'index.html', context)
