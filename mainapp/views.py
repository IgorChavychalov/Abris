from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import Draw, UserDraw, Polygons
# Create your views here.


def index(request):
    context = {
        "page_title":  "Главная"
    }
    return render(request, 'mainapp/index.html', context)


def draw_list(request):
    blueprints = request.user.user_draw.all()


    # blueprints = [
    #     {
    #         "name": "чертёж-1",
    #         "forestry": "Пригородное",
    #         "quarter": "11",
    #         "letter": "11"
    #     }
    # ]
    context = {
        "page_title": "Чертежи",
        "blueprints": blueprints,
    }

    return render(request, 'mainapp/draw-list.html', context)


def draw(request, pk):
    get_draw = get_object_or_404(Draw, pk=pk)
    get_polygons = Polygons.objects.exclude(pk=get_draw.pk)
    coordinates = get_polygons[0].coordinates.split(',')

    context = {
        "page_title": "Чертежи",
        "object": get_polygons[0],
        "coordinates": coordinates
    }

    return render(request, 'mainapp/draw.html', context)
