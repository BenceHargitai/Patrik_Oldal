# Generated by Django 3.2.9 on 2022-07-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0011_auto_20220723_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kapcsolo',
            name='key',
        ),
        migrations.AddField(
            model_name='kepek',
            name='felirat',
            field=models.CharField(default='Ha', max_length=30),
            preserve_default=False,
        ),
    ]
