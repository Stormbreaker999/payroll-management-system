# Generated by Django 3.1.5 on 2023-12-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_bank_details_transactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Contact',
            field=models.BigIntegerField(verbose_name='Contact_No'),
        ),
    ]