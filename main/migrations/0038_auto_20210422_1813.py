# Generated by Django 3.1.5 on 2021-04-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20210422_1225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='searchresult',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='subscribe',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='subscribe',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
