# Generated by Django 3.1.5 on 2023-12-12 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20231211_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_details',
            name='Accno',
            field=models.BigIntegerField(verbose_name='Account No'),
        ),
    ]
