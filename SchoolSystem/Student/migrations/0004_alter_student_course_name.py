# Generated by Django 3.2.4 on 2021-08-19 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_alter_student_medical_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]