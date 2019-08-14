from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')


def draw_list(request):
    return render(request, 'mainapp/draw-list.html')
