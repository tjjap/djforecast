# Generated by Django 3.2.4 on 2021-06-13 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=2, verbose_name='Level')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Weight')),
            ],
        ),
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directorate', models.CharField(choices=[('Public-1', 'Public-1'), ('Public-2', 'Public-2'), ('Public-3', 'Public-3'), ('Private-1', 'Private-1'), ('Private-2', 'Private-2')], max_length=10, verbose_name='Directorate')),
                ('ambm', models.CharField(max_length=30, verbose_name='AM/BM Name')),
                ('pid', models.CharField(max_length=10, unique=True, verbose_name='Prospect ID')),
                ('client', models.CharField(max_length=50, verbose_name='Client Name')),
                ('project', models.CharField(max_length=50, verbose_name='Project Name')),
                ('rental', models.BooleanField(default=False, verbose_name='Rental')),
                ('nmonth', models.IntegerField(default=1, verbose_name='x Months')),
                ('order_dd', models.DateField(verbose_name='SO Booking DD')),
                ('order_val', models.DecimalField(decimal_places=0, max_digits=14, verbose_name='Value')),
                ('gpm', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='GPM (%)')),
                ('bast_dd', models.DateField(verbose_name='BAST Date')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.level')),
            ],
            options={
                'verbose_name_plural': 'Sales Pipelines',
                'ordering': ['order_dd', 'level', '-order_val'],
            },
        ),
    ]
