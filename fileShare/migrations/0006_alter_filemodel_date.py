# Generated by Django 5.0.6 on 2024-06-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileShare', '0005_filemodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
