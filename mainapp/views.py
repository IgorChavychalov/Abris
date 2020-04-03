from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import Draw, UserDraw, Polygons
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import NewDrawForm
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.
import json
from django.urls import reverse
from django.template.context_processors import csrf


@login_required
def index(request):
    context = {
        "page_title":  "Главная",
        "blueprints": request.user.user_draw.all(),
    }
    return render(request, 'mainapp/index.html', context)


@login_required
def draw_add(request):
    if request.method == 'POST':
        form = NewDrawForm(data=request.POST)
        if form.is_valid():
            add_draw = Draw(name=request.POST['name'],
                            forestry=request.POST['forestry'],
                            quarter=request.POST['quarter'],
                            letter=request.POST['letter'])
            add_draw.save()
            user_draw = UserDraw(user=request.user,
                                 draw=add_draw,
                                 add_datetime=timezone.now())
            user_draw.save()

            polygon_add(add_draw)

            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = NewDrawForm()

    context = {
        "page_title": "Новый чертёж",
        'form': form,
    }
    return render(request, 'mainapp/draw_add.html', context)


@login_required
def draw_delete(request, pk):
    object = get_object_or_404(UserDraw, pk=pk).draw
    get_object_or_404(Draw, pk=object.pk).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def draw_read(request, pk):
    get_draw = get_object_or_404(UserDraw, pk=pk).draw
    get_polygons = Polygons.objects.filter(pk=get_draw.pk)
    if get_polygons:
        coordinates = get_polygons[0].coordinates.split(',')
    else:
        coordinates = []

    context = {
        "page_title": get_draw.name,
        "pk": pk,
        "coordinates": coordinates,
    }
    return render(request, 'mainapp/draw.html', context)


def polygon_add(draw, polygon_name='основной', operating=True):
    new_polygon = Polygons(draw=draw,
                           name=polygon_name,
                           coordinates=[],
                           operating=operating)
    new_polygon.save()


@login_required
def draw_update(request, pk):
    print(pk)
    if request.is_ajax():
        print(request)
        coordinates = request.GET.get('coordinates')
        print(coordinates)
        j_coordinates = json.loads(coordinates)
        data = list_to_string(j_coordinates)

        user_draw = get_object_or_404(UserDraw, pk=pk)
        draw_pk = user_draw.draw.pk
        new_coordinate = get_object_or_404(Polygons, pk=draw_pk)
        new_coordinate.coordinates = data
        new_coordinate.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def list_to_string(my_list):
    one_list = []
    for elem in my_list:
        one_list.append(str(elem[0]))
        one_list.append(str(elem[1]))

    result = ''
    for elem in one_list:
        if result == '':
            result += elem
        else:
            result += (',' + elem)
    return result


# @login_required
# def draw_add(request):
#     if request.is_ajax():
#         coordinates = request.GET.get('coordinates')
#         j_coordinates = json.loads(coordinates)
#         data = list_to_string(j_coordinates)
#
#         new_draw = Draw(name='Чертёж', forestry='Пригородное', quarter='100', letter='1')
#         new_draw.save()
#         new_polygon = Polygons(draw=new_draw, name='основной', coordinates=data, operating=True)
#         user_draw = UserDraw(user=request.user,
#                              draw=new_draw,
#                              add_datetime=timezone.now())
#         new_draw.save()
#         new_polygon.save()
#         user_draw.save()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#
#













# @login_required
# def draw_add(request):
#     if request.is_ajax():
#         coordinates = request.POST.get('coordinates')
#         j_coordinates = json.loads(coordinates)
#         data = list_to_string(j_coordinates)
#         print(data)
#         new_draw = Draw(name='Чертёж',
#                         forestry='Пригородное',
#                         quarter='100',
#                         letter='1')
#         new_draw.save()
#         new_polygon = Polygons(draw=new_draw,
#                                name='основной',
#                                coordinates=data,
#                                operating=True)
#         user_draw = UserDraw(user=request.user,
#                              draw=new_draw,
#                              add_datetime=timezone.now())
#         new_draw.save()
#         new_polygon.save()
#         user_draw.save()
#
#         print(f'что-то пришло {j_coordinates}')
#         pk = new_draw.pk
#         print(pk)
#
#         result = {}
#         result.update(csrf(request))
#
#         result['status'] = 'ok'
#         result['draw_id'] = pk
#         return JsonResponse(result)
#
#
#         # context = {
#         #     "page_title": "Чертежи",
#         #     "coordinates": data
#         # }
#     #     result = render_to_string('mainapp/draw.html', context)
#     # return JsonResponse({
#     #     'result': 'ок'
#     # })
#
#         # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#         # return HttpResponseRedirect(reverse('main:draw', kwargs={'pk': pk}))
#     # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))










# def filter(request):
#     if request.GET:
#         filter = request.GET.get('filter')
#         decoded_filter = json.loads(filter)  # из строки инициализирует объект
#         stations = Station.objects.all()
#
#         stations_out = []
#         for elem in stations:
#             stations_out.append({.......})  # создаем нужный объект
#
#         id_net = Net.objects.filter(name=decoded_filter["net"])
#         list_id_stations = Networkstations.objects.filter(idnet__in=id_net).values_list("idstation", flat=True)
#         list_name_net = []
#         if decoded_filter["net"] != 'all':
#             stations = stations.filter(id__in=list_id_stations)
#         if decoded_filter["type"] != 'all':
#             stations = stations.filter(type=decoded_filter["type"])
#         for station in stations:
#             list_name_net.append(
#                 list(Networkstations.objects.filter(idstation=station.id).values('idnet__name')))
#         ctx = {
#             'stations': stations_out,
#             'list_name_net': list_name_net,
#         }
#     return JsonResponse(ctx, safe=False)


