# Generated by Django 3.1.2 on 2020-10-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_apps', '0004_auto_20201004_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
