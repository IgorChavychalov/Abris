# Generated by Django 2.1.7 on 2019-08-17 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Draw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='название')),
                ('forestry', models.CharField(max_length=32, verbose_name='лесничество')),
                ('quarter', models.CharField(max_length=4, verbose_name='квартал')),
                ('letter', models.CharField(max_length=4, verbose_name='выдел')),
                ('rast', models.ImageField(blank=True, upload_to='rast')),
            ],
        ),
        migrations.CreateModel(
            name='Polygons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='название')),
                ('coordinates', models.TextField(null=True, verbose_name='координаты')),
                ('operating', models.BooleanField(default=True, verbose_name='основной')),
                ('draw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Draw')),
            ],
        ),
    ]
