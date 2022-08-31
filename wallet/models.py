from django.db import models
from django.utils import timezone


class Customer(models.Model):
    first_name=models.CharField(max_length=15,null=True)
    last_name=models.CharField(max_length=15,null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
         )
    gender = models.CharField(max_length=1, choices= GENDER_CHOICES,null=True)
    address=models.CharField(max_length=20,null=True)
    age=models.CharField(max_length=10,null=True)
    nationality=models.CharField(max_length=20,null=True)
    id_number=models.IntegerField(null=True)
    phonenumber=models.CharField(max_length=15,null=True)
    email=models.EmailField(max_length=25,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    STATUS_CHOICES = (
        ('M', 'Married'),
        ('S', 'Single'),
         )
    marital_status = models.CharField(max_length=1, choices=STATUS_CHOICES,null=True)
    signature = models.ImageField(upload_to='signature/',null=True)
    EMPLOYMENT_CHOICES = (
        ('W', 'Working'),
        ('N', 'Not Working'),
         )
   
    
    employment_status = models.CharField(max_length=1, choices=EMPLOYMENT_CHOICES,null=True)

class Currency(models.Model):
    amount=models.IntegerField(default=0)
    symbol=models.CharField(max_length=25, null=True)
    country_of_origin=models.CharField(max_length=25, null=True)

class Wallet(models.Model):
    customers=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Wallet_customers')
    pin=models.TextField(max_length=6,null=True)
    active=models.BooleanField(default=False)
    date_created=models.DateTimeField(default=timezone.now)
    
class Account(models.Model):
    account_type=models.CharField(max_length=20,null=True)
    account_Name=models.CharField(max_length=20,null=True)
    savings=models.IntegerField()
    destination=models.ForeignKey('Wallet',on_delete=models.CASCADE, related_name ='Account_Destination')

class Transaction(models.Model):
    transaction_type=models.CharField(max_length=10,null=True)
    transaction_charge=models.IntegerField()
    transaction_date=models.DateTimeField(default=timezone.now)
    original_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_original_account')
    destination_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_destination_account')

class Card(models.Model):
    date_Issued=models.DateTimeField(default=timezone.now)
    cvv_security_code=models.IntegerField()
    account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name ='Card_account') 
    signature = models.ImageField(upload_to='signature/',null=True)
    ISSUER_CHOICES=(
         ('Master', 'Mastercard'),
        ('visa', 'visacard'),
    )
    
class ThirdParty(models.Model):
    fullname=models. CharField(max_length=15,null=True)
    email=models.EmailField(max_length=25,null=True)
    phone_Number=models.IntegerField()
    transaction_cost=models. IntegerField()
    account=models.ForeignKey('account', on_delete=models.CASCADE, related_name ='ThirdParty_account')
    active=models.BooleanField()

class Notification(models.Model):
    date_created=models.DateTimeField(default=timezone.now)
    active=models.BooleanField()  
    image = models.ImageField(upload_to='image_pictures/',null=True)

class Receipt(models.Model):
    receipt_date=models.DateTimeField(default=timezone.now)
    transaction=models.ForeignKey('transaction', on_delete=models.CASCADE, related_name ='Receipt_Transaction')
    recipt_File=models.FileField(upload_to='wallet/')
    recipt_number=models.CharField(max_length=25, null=True)
    total_Amount=models.IntegerField(default=0)
    
class Loan(models.Model):
    loan_type=models.CharField(max_length=25, null=True)
    amount=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    loan_term=models.IntegerField()
    due_date=models.DateField(default=timezone.now)
    guaranter=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Loan_guaranter')
    loan_balance=models.IntegerField()
    interest_rate=models.IntegerField()

class Reward(models.Model): 
    points=models.CharField(max_length=25, null=True)
    date=models.DateTimeField(default=timezone.now) 
    transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name ='Reward_transaction')
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Reward_customer')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
         )
    gender = models.CharField(max_length=1, choices= GENDER_CHOICES,null=True)