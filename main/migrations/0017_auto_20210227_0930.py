# Generated by Django 3.1.5 on 2021-02-27 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0016_auto_20210227_0921'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SchoolExamResult',
            new_name='AlevelExamResult',
        ),
        migrations.CreateModel(
            name='OlevelExamResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('year', models.PositiveIntegerField()),
                ('division_one', models.PositiveIntegerField()),
                ('division_two', models.PositiveIntegerField()),
                ('division_three', models.PositiveIntegerField()),
                ('division_four', models.PositiveIntegerField()),
                ('division_zero', models.PositiveIntegerField()),
                ('dv1T', models.PositiveIntegerField(blank=True, null=True)),
                ('dv2T', models.PositiveIntegerField(blank=True, null=True)),
                ('dv3T', models.PositiveIntegerField(blank=True, null=True)),
                ('dv4T', models.PositiveIntegerField(blank=True, null=True)),
                ('dv0T', models.PositiveIntegerField(blank=True, null=True)),
                ('dv1P', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('dv2P', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('dv3P', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('dv4P', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('dv0P', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_point', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.school')),
            ],
        ),
    ]
