from .models import Movie

def movie_list(request):
  movies = Movies.objects.all()
  return {"movies_list":movies}
