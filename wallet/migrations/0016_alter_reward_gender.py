# Generated by Django 4.0.6 on 2022-08-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0015_reward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]