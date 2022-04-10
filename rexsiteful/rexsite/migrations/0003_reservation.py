# Generated by Django 4.0.3 on 2022-04-06 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rexsite', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.TimeField(default='14:30')),
                ('endtime', models.TimeField(default='14:30')),
                ('court', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='court', to='rexsite.courts')),
                ('firstname', models.ForeignKey(default='john', on_delete=django.db.models.deletion.CASCADE, related_name='firstname', to=settings.AUTH_USER_MODEL)),
                ('lastname', models.ForeignKey(default='doe', on_delete=django.db.models.deletion.CASCADE, related_name='lastname', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
