# Generated by Django 3.2.4 on 2021-09-02 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='profile',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
