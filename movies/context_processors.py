from .models import Movie

def movie_list(request):
  movies = Movie.objects.all()
  return {"movies_list":movies}
