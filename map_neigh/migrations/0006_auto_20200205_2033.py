# Generated by Django 2.2b1 on 2020-02-05 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_neigh', '0005_announcement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='anouncement_type',
        ),
        migrations.AddField(
            model_name='announcement',
            name='announcement_type',
            field=models.CharField(choices=[('announcement', 'Announcement'), ('alert', 'Alert'), ('offer', 'Offer')], default='announcement', max_length=12),
        ),
    ]
