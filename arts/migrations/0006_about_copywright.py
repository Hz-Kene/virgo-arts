# Generated by Django 3.1.5 on 2021-12-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0005_virgo_map_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='copywright',
            field=models.TextField(null=True),
        ),
    ]
