# Generated by Django 3.1.6 on 2021-02-15 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0002_category_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Telefon', 'Telefon,Planset'), ('Məişət texnikası', 'Məişət texnikası'), ('Tv auidio Foto və Əyləncə', 'Tv auidio Foto və Əyləncə'), ('Kompüter Texnikasi', 'Kompüter Texnikasi'), ('Aksesuarlar', 'Aksesuarlar'), ('Outlet', 'Outlet')], max_length=200)),
                ('name', models.CharField(max_length=220)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]