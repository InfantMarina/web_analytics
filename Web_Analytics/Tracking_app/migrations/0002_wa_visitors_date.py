# Generated by Django 3.1.6 on 2021-04-10 13:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wa_visitors',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
