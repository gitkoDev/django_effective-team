# Generated by Django 5.0.4 on 2024-04-25 01:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0006_transaction_receiver_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='sender_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team_app.creator'),
        ),
    ]