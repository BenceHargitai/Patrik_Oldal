# Generated by Django 3.2.9 on 2022-07-26 11:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0016_auto_20220726_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fooldal',
            options={'verbose_name': 'Fooldal', 'verbose_name_plural': 'Fooldal'},
        ),
        migrations.AlterField(
            model_name='fooldal',
            name='text',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
