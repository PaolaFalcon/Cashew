from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', Index, name='index'),
    # CATEGORIES
    url(r'^categories/$', CategoryListView.as_view(), name='categories'),
    url(r'^category_create/$', CategoryCreateView.as_view(), name='category_create'),
    url(r'^category_update/(?P<pk>[0-9]+)/$', CategoryUpdateView.as_view(), name='category_update'),
    url(r'^category_delete/(?P<pk>[0-9]+)/$', CategoryDeleteView.as_view(), name='category_delete'),
    # TRANSACTIONS
    url(r'^transactions/$', TransactionListView.as_view(), name='transactions'),
    url(r'^transaction_create/$', TransactionCreateView.as_view(), name='transaction_create'),
    url(r'^transaction_update/(?P<pk>[0-9]+)/$', TransactionUpdateView.as_view(), name='transaction_update'),
    url(r'^transaction_delete/(?P<pk>[0-9]+)/$', TransactionDeleteView.as_view(), name='transaction_delete'),
    # ACCOUNTS
    url(r'^accounts/$', AccountListView.as_view(), name='accounts'),
    url(r'^account_create/$', AccountCreateView.as_view(), name='account_create'),
    url(r'^account_update/(?P<pk>[0-9]+)/$', AccountUpdateView.as_view(), name='account_update'),
    url(r'^account_delete/(?P<pk>[0-9]+)/$', AccountDeleteView.as_view(), name='account_delete'),
]
