from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'year_born': 666,
        'city_born': 'Moscow',
        'movie_name': 'Dungeon Master',

    }
    return render(request, 'actors/bio.html', context=data)
