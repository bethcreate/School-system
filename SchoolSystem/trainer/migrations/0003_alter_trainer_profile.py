# Generated by Django 3.2.4 on 2021-09-02 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0002_auto_20210819_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='profile',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
