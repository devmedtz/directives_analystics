# Generated by Django 3.1.5 on 2021-02-27 10:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0018_auto_20210227_1040'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AlevelExamRank',
            new_name='ExamRank',
        ),
        migrations.RenameModel(
            old_name='OlevelExamResult',
            new_name='ExamResult',
        ),
        migrations.RemoveField(
            model_name='olevelexamrank',
            name='school',
        ),
        migrations.DeleteModel(
            name='AlevelExamResult',
        ),
        migrations.DeleteModel(
            name='OlevelExamRank',
        ),
    ]
