# Generated by Django 4.0.6 on 2022-08-25 10:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0013_receipts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(max_length=25, null=True)),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('loan_term', models.IntegerField()),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('loan_balance', models.IntegerField()),
                ('interest_rate', models.IntegerField()),
                ('guaranter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Loan_guaranter', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('recipt_File', models.FileField(upload_to='wallet/')),
                ('recipt_number', models.CharField(max_length=25, null=True)),
                ('total_Amount', models.IntegerField(default=0)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receipt_Transaction', to='wallet.transaction')),
            ],
        ),
        migrations.RenameModel(
            old_name='Notifications',
            new_name='Notification',
        ),
        migrations.DeleteModel(
            name='Receipts',
        ),
    ]
