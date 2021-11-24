# Generated by Django 3.2.9 on 2021-11-23 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('cast', models.CharField(max_length=1024)),
                ('duration_min', models.IntegerField()),
                ('certification_label', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_name', models.CharField(max_length=32)),
                ('available_seats', models.IntegerField()),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('theatre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.theatre')),
            ],
        ),
    ]
