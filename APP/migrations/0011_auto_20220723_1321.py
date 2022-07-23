# Generated by Django 3.2.9 on 2022-07-23 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0010_kepek'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kepek',
            name='felirat',
        ),
        migrations.CreateModel(
            name='Kapcsolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('felirat', models.CharField(max_length=15)),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.projekt')),
            ],
        ),
    ]
