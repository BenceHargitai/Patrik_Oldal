# Generated by Django 3.2.9 on 2022-07-20 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_projekt_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='projekt',
            name='url',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]