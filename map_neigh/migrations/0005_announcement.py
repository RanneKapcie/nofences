# Generated by Django 2.2b1 on 2020-02-04 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map_neigh', '0004_auto_20200122_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1500)),
                ('anouncement_type', models.CharField(choices=[('announcement', 'announcement'), ('alert', 'alert'), ('offer', 'offer')], default='announcement', max_length=12)),
                ('date', models.DateField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map_neigh.Buildings')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
