
# Create your views here.
from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse


def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)


def movie_details(request, k):

    movie = Movie.objects.get(pk=k)
    data = {
        'name': movie.name,
        'description': movie.about,
        'active': movie.active
    }
    return JsonResponse(data)