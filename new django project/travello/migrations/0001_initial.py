# Generated by Django 4.2 on 2023-05-04 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='pics')),
                ('days', models.TextField()),
                ('person', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
    ]