from django.core.management.base import BaseCommand
from mainapp.models import Draw, Polygons, UserDraw
from django.contrib.auth.models import User
from authapp.models import User

import os
import json

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        draw_file = load_from_json('draw')

        Draw.objects.all().delete()
        for elem in draw_file:
            Draw.objects.create(**elem)

        polygons_file = load_from_json('polygons')

        Polygons.objects.all().delete()
        for elem in polygons_file:
            draw_name = elem["draw"]
            # Получаем категорию по имени
            _draw = Draw.objects.get(name=draw_name)
            # Безопасный аналог
            # _category = ProductCategory.objects.filter(name=category_name).first()
            # Заменяем название категории объектом
            elem['draw'] = _draw
            Polygons.objects.create(**elem)

        # # Создаем суперпользователя при помощи менеджера модели
        if not User.objects.filter(username='abris').exists():
            User.objects.create_superuser('abris', 'abris@mail.ru', 'abris1379')

        userdraw_file = load_from_json('userdraw')
        for elem in userdraw_file:
            UserDraw.objects.create(**elem)



