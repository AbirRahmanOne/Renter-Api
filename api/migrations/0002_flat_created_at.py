# Generated by Django 3.2.5 on 2021-07-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]