# Generated by Django 3.1.1 on 2020-12-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20201230_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='otp_customer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='otp_restro',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='prepared',
            field=models.BooleanField(default=False),
        ),
    ]