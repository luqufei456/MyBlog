# Generated by Django 2.0.2 on 2018-02-13 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='acontent',
            field=models.TextField(blank=True, null=True),
        ),
    ]
