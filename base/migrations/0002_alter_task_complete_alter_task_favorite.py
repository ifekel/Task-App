# Generated by Django 4.1.2 on 2023-01-11 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='favorite',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]