# Generated by Django 4.2.4 on 2023-09-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_remove_companyprofile_criteria_jobs_criteria'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='companydp',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
