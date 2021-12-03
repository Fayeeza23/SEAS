# Generated by Django 3.2.9 on 2021-12-03 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seasapp', '0008_alter_course_t_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='course_t',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='CoOfferedCourse_T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COFFERED_WITH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='COFFERED_WITH', to='seasapp.course_t')),
                ('OfferedCourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OFFERED_COURSE_ID', to='seasapp.course_t')),
            ],
        ),
        migrations.RemoveField(
            model_name='course_t',
            name='CoOfferdCourse',
        ),
    ]
