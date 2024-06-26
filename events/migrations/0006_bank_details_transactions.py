# Generated by Django 3.1.5 on 2023-12-10 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_delete_dep2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('Sno', models.IntegerField(primary_key=True, serialize=False, verbose_name='S.No.')),
                ('Attendance', models.IntegerField(verbose_name='Attendance')),
                ('PDate', models.DateField(verbose_name='Payment Date')),
                ('Basic', models.IntegerField(verbose_name='Basic_Salary')),
                ('HRA', models.IntegerField(verbose_name='HRA')),
                ('TA', models.IntegerField(verbose_name='TA')),
                ('DA', models.IntegerField(verbose_name='DA')),
                ('PF', models.IntegerField(verbose_name='PF')),
                ('IT', models.IntegerField(verbose_name='IT')),
                ('DID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.department')),
                ('ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Bank_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accno', models.IntegerField(verbose_name='Account No')),
                ('IFSC', models.CharField(max_length=12, verbose_name='IFSC Code')),
                ('ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.employee')),
            ],
        ),
    ]
