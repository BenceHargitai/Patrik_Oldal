# Generated by Django 3.2.9 on 2022-07-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0014_alter_kapcsolo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kapcsolo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
