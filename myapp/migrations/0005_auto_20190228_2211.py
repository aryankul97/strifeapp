# Generated by Django 2.1.4 on 2019-02-28 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_canmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcomp',
            name='MarksPerQues',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addcomp',
            name='MaxMarks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addcomp',
            name='Number_Ques',
            field=models.IntegerField(default=12233),
            preserve_default=False,
        ),
    ]
