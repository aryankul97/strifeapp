# Generated by Django 2.0.2 on 2019-03-08 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='newadmin',
            name='Paid',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
