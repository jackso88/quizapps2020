# Generated by Django 3.1.2 on 2020-10-04 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_apps', '0006_auto_20201004_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(),
        ),
    ]
