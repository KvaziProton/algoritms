# Generated by Django 2.0.7 on 2018-07-20 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tr_helper', '0004_auto_20180719_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logger',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='logger',
            name='decision',
        ),
        migrations.AddField(
            model_name='testlog',
            name='decision',
            field=models.CharField(blank=True, choices=[('0', 'new'), ('1', 'update'), ('2', 'user-choice'), ('3', 'found-version')], default=0, max_length=2, null=True),
        ),
    ]
