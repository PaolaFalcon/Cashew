from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, ListView, DetailView, FormView, UpdateView, CreateView, DeleteView
from fm.views import AjaxCreateView, AjaxUpdateView, AjaxDeleteView
from .models import *
from .forms import *
from django.db.models import *
from money import Money
from django.db.models import Q
from dateutil.relativedelta import *

def Index(request):
    type_to_ignore = 2 # Credit card
    default_locale = 'en_US'
    default_short_name = 'MXN'
    queryset = Account.objects.all()
    # Account summary
    account_summary = Account.objects.all().annotate(amount=Sum('transaction__amount')).select_related('type','currency')
    for obj in account_summary: obj.formatted_amount = Money(obj.amount, obj.currency.short_name).format(obj.currency.locale, '$#,##0.00')
    # Balance TODO: ignores currency
    balance_without_debt = Money(sum(c.amount for c in account_summary if c.type.id != type_to_ignore), default_short_name).format(default_locale, '$#,##0.00')
    balance_with_debt = Money(sum(c.amount for c in account_summary), default_short_name).format(default_locale, '$#,##0.00')
    last_transactions = Transaction.objects.all().select_related('account','category','account__type','account__currency').order_by('-date','-id')[:5]
    return render(request, "cashewapp/index.html", {
        'account_summary' : account_summary,
        'last_transactions' : last_transactions,
        'balance_without_debt' : balance_without_debt,
        'balance_with_debt' : balance_with_debt,
        })

# CATEGORIES

class CategoryListView(ListView):
    model = Category
    template_name = 'cashewapp/categories.html'
    def get_queryset(self):
        return Category.objects.all().filter(active=True).order_by('name')

class CategoryCreateView(AjaxCreateView):
    form_class = CategoryForm

class CategoryUpdateView(AjaxUpdateView):
    message_template = "cashewapp/category_instance.html"
    form_class = CategoryForm
    model = Category
    pk_url_kwarg = 'pk'

class CategoryDeleteView(AjaxDeleteView):
    model = Category
    pk_url_kwarg = 'pk'

# TRANSACTIONS

class TransactionListView(ListView):
    model = Transaction
    template_name = 'cashewapp/transactions.html'
    start_date = datetime.date(datetime.date.today().year, datetime.date.today().month, 1)
    end_date = datetime.date.today() + relativedelta(day=1, months=+1, days=-1)
    account = 0
    category = 0

    def get_queryset(self):
        if(self.request.GET.get('btn_filter')):
            self.account = int(self.request.GET.get('accounts'))
            self.start_date = datetime.datetime.strptime(self.request.GET.get('start_date'), '%Y-%m-%d')
            self.end_date = datetime.datetime.strptime(self.request.GET.get('end_date'), '%Y-%m-%d')
            self.category = int(self.request.GET.get('categories'))
            # Filters
            object_list = Transaction.objects.all().filter(date__range=(self.start_date,self.end_date)).select_related('account','category','account__type','account__currency').order_by('-date','-id')
            if(self.category != 0):
                object_list = object_list.filter(category__id=self.category)
            if(self.account != 0):
                object_list = object_list.filter(account__id=self.account)
        else:
            object_list = Transaction.objects.all().filter(date__range=(self.start_date,self.end_date)).select_related('account','category','account__type','account__currency').order_by('-date','-id')

        return object_list
    def get_context_data(self, **kwargs):
        context = super(TransactionListView, self).get_context_data(**kwargs)
        context['accounts'] = Account.objects.all()
        context['categories'] = Category.objects.all().filter(active=True).order_by('name')
        context['f_start_date'] = self.start_date.strftime('%Y-%m-%d')
        context['f_end_date'] = self.end_date.strftime('%Y-%m-%d')
        context['f_category'] = self.category
        context['f_account'] = self.account
        return context

class TransactionCreateView(AjaxCreateView):
    form_class = TransactionForm

class TransactionUpdateView(AjaxUpdateView):
    message_template = "cashewapp/transaction_instance.html"
    form_class = TransactionForm
    model = Transaction
    pk_url_kwarg = 'pk'

class TransactionDeleteView(AjaxDeleteView):
    model = Transaction
    pk_url_kwarg = 'pk'

# ACCOUNTS

class AccountListView(ListView):
    model = Account
    template_name = 'cashewapp/accounts.html'
    def get_queryset(self):
        return Account.objects.all().select_related('type','currency')

class AccountCreateView(AjaxCreateView):
    form_class = AccountForm
    model = Account

class AccountUpdateView(AjaxUpdateView):
    message_template = "cashewapp/account_instance.html"
    form_class = AccountForm
    model = Account
    pk_url_kwarg = 'pk'

class AccountDeleteView(AjaxDeleteView):
    model = Account
    pk_url_kwarg = 'pk'
