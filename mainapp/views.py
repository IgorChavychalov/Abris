from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "page_title":  "Главная"
    }
    return render(request, 'mainapp/index.html', context)


def draw_list(request):
    blueprints = [
        {
            "name": "чертёж-1",
            "forestry": "Пригородное",
            "quarter": "11",
            "letter": "11"
        }
    ]
    context = {
        "page_title": "Чертежи",
        "blueprints": blueprints
    }

    return render(request, 'mainapp/draw-list.html', context)
