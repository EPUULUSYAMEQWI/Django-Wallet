# Generated by Django 4.0.6 on 2022-08-25 10:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0012_notifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('recipt_File', models.FileField(upload_to='wallet/')),
                ('recipt_number', models.CharField(max_length=25, null=True)),
                ('total_Amount', models.IntegerField(default=0)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receipts_Transaction', to='wallet.transaction')),
            ],
        ),
    ]
