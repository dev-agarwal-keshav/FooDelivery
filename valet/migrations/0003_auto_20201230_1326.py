# Generated by Django 3.1.1 on 2020-12-30 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valet', '0002_valet_free'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valet',
            name='work_hr',
            field=models.CharField(choices=[('10AM-10PM', '10AM-10PM'), ('10PM-10AM', '10PM-10AM')], default='10AM-10PM', max_length=100),
        ),
    ]
