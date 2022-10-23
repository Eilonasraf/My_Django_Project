from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=500)
    discription = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='images/', null=True)
    screen_shot = models.ImageField(upload_to='screenshots/')
    movie_length = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    movie_rate = models.CharField(max_length=100)
    imdb_raiting = models.CharField(max_length=100)
    movie_director = models.CharField(max_length=200)
    movie_actor = models.CharField(max_length=1000)
    movie_language = models.CharField(max_length=100)
    movie_quality = models.CharField(max_length=100)
    movie_size = models.CharField(max_length=100)
    movie_suitable = models.CharField(max_length=100)
    movie_link = models.TextField(max_length=10000)
    movie_online = models.TextField(max_length=1000)
    movie_type = models.CharField(max_length=700)
    movie_subscription = models.CharField(max_length=700)
    movie_category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def snippet(self):
        return self.discription[:10] + '...'
