# Generated by Django 3.1.1 on 2020-12-30 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('valet', '0003_auto_20201230_1326'),
        ('customer', '0004_auto_20201230_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='valet',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='valet', to='valet.valet'),
        ),
    ]
