# Generated by Django 3.1.5 on 2021-02-18 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210217_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='school_type',
            new_name='ownership',
        ),
        migrations.RemoveField(
            model_name='school',
            name='alevel_exam_results_review',
        ),
        migrations.RemoveField(
            model_name='school',
            name='olevel_exam_results_review',
        ),
    ]
