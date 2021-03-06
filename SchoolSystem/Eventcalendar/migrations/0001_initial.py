# Generated by Django 3.2.4 on 2021-08-12 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100, null=True)),
                ('event_date', models.DateField(null=True)),
                ('event_time', models.TimeField(null=True)),
                ('event_planner', models.CharField(max_length=100, null=True)),
                ('event_participants', models.CharField(max_length=200, null=True)),
                ('event_duration', models.TimeField(null=True)),
                ('event_approved_by', models.CharField(max_length=50, null=True)),
                ('event_id', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
