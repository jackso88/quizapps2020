# Generated by Django 3.1.2 on 2020-10-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_apps', '0007_auto_20201004_1211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name_plural': 'questions'},
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(),
        ),
    ]
