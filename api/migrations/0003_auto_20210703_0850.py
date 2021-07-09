# Generated by Django 3.2.5 on 2021-07-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_flat_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='renter_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]