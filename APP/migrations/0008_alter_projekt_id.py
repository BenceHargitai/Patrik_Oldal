# Generated by Django 3.2.9 on 2022-07-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0007_remove_projekt_projektszam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projekt',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
