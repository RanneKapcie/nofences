# Generated by Django 2.2b1 on 2020-02-05 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map_neigh', '0007_auto_20200205_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='building_id',
            field=models.ForeignKey(db_column='building_id', on_delete=django.db.models.deletion.CASCADE, to='map_neigh.Buildings'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='user_name',
            field=models.ForeignKey(db_column='user_name', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
