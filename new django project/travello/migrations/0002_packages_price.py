# Generated by Django 4.2 on 2023-05-04 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]