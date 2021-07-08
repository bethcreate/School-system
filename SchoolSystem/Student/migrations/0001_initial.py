# Generated by Django 3.2.4 on 2021-07-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=15)),
                ('age', models.PositiveSmallIntegerField(max_length=3)),
                ('date_of_birth', models.DateField(max_length=27)),
            ],
        ),
    ]
