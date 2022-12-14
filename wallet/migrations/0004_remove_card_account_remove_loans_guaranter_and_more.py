# Generated by Django 4.0.6 on 2022-08-25 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_alter_customer_employment_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='account',
        ),
        migrations.RemoveField(
            model_name='loans',
            name='guaranter',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='receipts',
            name='transaction',
        ),
        migrations.RemoveField(
            model_name='reward',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='reward',
            name='transaction',
        ),
        migrations.RemoveField(
            model_name='thirdparty',
            name='account',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='destination_account',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='original_account',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='receipt',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.DeleteModel(
            name='Loans',
        ),
        migrations.DeleteModel(
            name='Notifications',
        ),
        migrations.DeleteModel(
            name='Receipts',
        ),
        migrations.DeleteModel(
            name='Reward',
        ),
        migrations.DeleteModel(
            name='ThirdParty',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
    ]
