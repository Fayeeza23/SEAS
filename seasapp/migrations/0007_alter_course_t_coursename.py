# Generated by Django 3.2.9 on 2021-12-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasapp', '0006_alter_course_t_coursename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_t',
            name='CourseName',
            field=models.CharField(max_length=100),
        ),
    ]
