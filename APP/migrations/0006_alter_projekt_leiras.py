# Generated by Django 3.2.9 on 2022-07-21 12:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0005_alter_projekt_projektszam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projekt',
            name='leiras',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]