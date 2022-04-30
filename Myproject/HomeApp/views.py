from django.shortcuts import render
from Movies import models
# Create your views here.
def MainHome (request):
    return render(request, template_name='MainHome.html')

def home (request):
    user = request.user
    Movies_obj = models.Movies.objects.all()
    return render(request, 'home.html', {'user': user, 'movies1': Movies_obj[:4], 'movies2': Movies_obj[4:8], 'movies3': Movies_obj[8:12]})