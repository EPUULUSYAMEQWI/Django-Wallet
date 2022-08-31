
from locale import currency
from django.contrib import admin

from .models import Customer,Wallet,Account,Transaction,Card,ThirdParty ,Notification ,Receipt,Loan,Reward,Currency
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','age','email',)
    search_fields=('first_name','last_name',)
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=('customers','pin','active',)
    search_fields=('customers','pin',)
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=('account_type','account_Name','savings','destination',)
    search_fields=('account_type','account_Name',)
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=('transaction_type','transaction_charge','transaction_date','original_account',)
    search_fields=('transaction_type','transaction_date',)
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=('date_Issued','cvv_security_code','account','signature',)
    search_fields=('date_Issued','cvv_security_code',)
admin.site.register(Card,CardAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display=('fullname','email','phone_Number','transaction_cost',)
    search_fields=('fullname','email',)
admin.site.register(ThirdParty,ThirdPartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=('date_created','active','image',)
    search_fields=('date_created','active',)
admin.site.register(Notification,NotificationAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display=('receipt_date','transaction','recipt_File','recipt_number')
    search_fields=('receipt_date','transaction','recipt_File')
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=('loan_type','amount','date','loan_term')
    search_fields=('loan_type','date')
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=('points','date','transaction','customer','gender')
    search_fields=('points','date')
admin.site.register(Reward,RewardAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display=('amount','symbol','country_of_origin')
    search_fields=('amount','symbol')
admin.site.register(Currency,CurrencyAdmin)
