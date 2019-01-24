from django import forms
from django.conf import settings
from django.utils import timezone
from django.forms import extras
from .models import *
from mptt.forms import TreeNodeChoiceField

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['parent','name']

class TransactionForm(forms.ModelForm):
    category = TreeNodeChoiceField(queryset=Category.objects.all(), required=False)
    class Meta:
        model = Transaction
        fields = ['date','category','account','amount','note','keywords']
        widgets = {
        'date': forms.DateTimeInput(format='%Y-%m-%d',attrs={
            'class':'datepicker'
            })
        }

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name','type','currency']
