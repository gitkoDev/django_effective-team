# Generated by Django 5.0.4 on 2024-04-25 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0009_rename_receiver_id_transaction_receiver_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]