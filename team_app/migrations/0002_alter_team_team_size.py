# Generated by Django 5.0.4 on 2024-05-03 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_size',
            field=models.IntegerField(default=2),
        ),
    ]