# Generated by Django 3.1.5 on 2021-04-22 05:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_region_districts'),
        ('main', '0034_searchresult_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchresult',
            name='phone',
        ),
        migrations.AddField(
            model_name='searchresult',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='accomodation_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='class_size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscribe',
            name='curricular_system',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.district'),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='fee_from',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='fee_to',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='no_fee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='ownership',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.region'),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='school_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='school_multicultural',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='school_subjects',
            field=models.ManyToManyField(blank=True, to='main.SchoolSubject'),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='subject_combination',
            field=models.ManyToManyField(blank=True, to='main.SubjectCombination'),
        ),
        migrations.AlterField(
            model_name='searchresult',
            name='school',
            field=models.ManyToManyField(blank=True, related_name='schools', to='main.School'),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='school',
        ),
        migrations.AddField(
            model_name='subscribe',
            name='school',
            field=models.ManyToManyField(null=True, to='main.School'),
        ),
    ]