from django.db import models
from django.core.validators import validate_comma_separated_integer_list
# from django.contrib.gis.db import models


class Draw(models.Model):
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    forestry = models.CharField(verbose_name='лесничество', max_length=32)
    quarter = models.CharField(verbose_name='квартал', max_length=4)
    letter = models.CharField(verbose_name='выдел', max_length=4)
    # rast = models.RasterField()
    rast = models.ImageField(upload_to='rast', blank=True)

    def __str__(self):
        return f"{self.name} {self.forestry} {self.quarter}-{self.letter}"


class Polygons(models.Model):
    draw = models.ForeignKey(Draw, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название', max_length=64)
    # coordinates = models.LineStringField()
    coordinates = models.TextField(verbose_name='координаты', null=True)
    # coordinates = models.CommaSeparatedIntegerField(verbose_name='координаты', max_length=600)
    operating = models.BooleanField(verbose_name='основной', default=True)

    def __str__(self):
        return f"{self.name} {self.operating}"
