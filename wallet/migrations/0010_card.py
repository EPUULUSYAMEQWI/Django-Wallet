# Generated by Django 4.0.6 on 2022-08-25 09:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0009_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_Issued', models.DateTimeField(default=django.utils.timezone.now)),
                ('cvv_security_code', models.IntegerField()),
                ('signature', models.ImageField(null=True, upload_to='signature/')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_account', to='wallet.account')),
            ],
        ),
    ]