# Generated by Django 3.0.3 on 2020-09-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_remove_reserveinfo_when'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserveinfo',
            name='Timing',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
