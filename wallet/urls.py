
from django.urls import path
from.views import register_customer
from.views import register_currency
from.views import register_wallet
from.views import register_account
from.views import register_transaction
from.views import register_card
from.views import register_thirdparty
from.views import register_notification
from.views import register_receipt
from.views import register_loan
from.views import register_reward






urlpatterns = [
    path("registerCustomer/",register_customer,name="registration"),
    path("registerCurrency/",register_currency,name="registration"),
    path("registerWallet/",register_wallet,name="registration"),
    path("registerAccount/",register_account,name="registration"),
    path("registerTranscation/",register_transaction,name="registration"),
    path("registerCard/",register_card,name="registration"),
    path("registerThirdparty/",register_thirdparty,name="registration"),
    path("registerNotifiacation/",register_notification,name="registration"),
    path("registerReceipt/",register_receipt,name="receipt"),
    path("registerLoan/",register_loan,name="receipt"),
    path("registerReward/",register_reward,name="receipt"),

]












