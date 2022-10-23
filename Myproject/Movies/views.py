from django.shortcuts import render
from docutils.utils.math.latex2mathml import mo
from scipy.interpolate import interp1d

from Movies.models import Movies as MoviesModel

# Create your views here.
def Movies (request):
    return render(request, 'Movies.html')

def movie_details(request, movie_id):
    movies_obj = MoviesModel
    get_movie = MoviesModel.objects.filter(id=movie_id)
    return render(request, 'movie_details.html', {'movies': get_movie})
