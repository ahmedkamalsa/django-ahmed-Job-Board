# Generated by Django 4.2.4 on 2023-08-31 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Vacancy',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
