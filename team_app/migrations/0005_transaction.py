# Generated by Django 5.0.4 on 2024-04-25 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0004_rename_member_name_request_member_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_id', models.IntegerField(default=0)),
            ],
        ),
    ]