# Generated by Django 3.2.4 on 2021-06-16 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='level',
            options={'ordering': ['ordering'], 'verbose_name_plural': 'Levels'},
        ),
        migrations.AddField(
            model_name='level',
            name='ordering',
            field=models.IntegerField(null=True, verbose_name='Ordering'),
        ),
    ]
