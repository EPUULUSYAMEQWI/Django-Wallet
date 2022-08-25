# Generated by Django 4.0.6 on 2022-08-25 10:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0011_thirdparty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField()),
                ('image', models.ImageField(null=True, upload_to='image_pictures/')),
            ],
        ),
    ]