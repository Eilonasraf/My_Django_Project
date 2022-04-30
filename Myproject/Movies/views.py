from django.shortcuts import render

# Create your views here.
def Movies (request):
    return render(request, 'Movies.html')