# Generated by Django 3.1.5 on 2021-12-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0002_rename_arts_art'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='about',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='about',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='art',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='virgo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
