# Generated by Django 3.2.9 on 2021-11-24 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20211124_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theatre',
            name='city',
            field=models.CharField(choices=[('DELHI', 'Delhi'), ('KOLKATA', 'Kolkata'), ('MUMBAI', 'Mumbai'), ('CHENNAI', 'Chennai'), ('BANGALORE', 'Bangalore'), ('HYDERABAD', 'Hyderabad')], default='', max_length=9),
        ),
    ]
