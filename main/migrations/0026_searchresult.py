# Generated by Django 3.1.5 on 2021-04-18 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20210418_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('accomodation_type', models.CharField(blank=True, max_length=100, null=True)),
                ('class_size', models.CharField(blank=True, max_length=100, null=True)),
                ('ownership', models.CharField(blank=True, max_length=100, null=True)),
                ('school_multicultural', models.CharField(blank=True, max_length=100, null=True)),
                ('school_location', models.CharField(blank=True, max_length=100, null=True)),
                ('curricular_system', models.CharField(blank=True, max_length=100, null=True)),
                ('school_subjects', models.CharField(blank=True, max_length=200, null=True)),
                ('subject_combination', models.CharField(blank=True, max_length=100, null=True)),
                ('average_tution_fee', models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True)),
                ('no_fee', models.BooleanField(default=False)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=14, null=True)),
            ],
        ),
    ]
