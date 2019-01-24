from django.db import models
from money import Money
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
import sys
from django_enumfield import enum

# Text to be formatted for transfer categories
TRANSFER_NAME = "[Transfer to {0}]"

class Category(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, default=None, related_name='children', db_index=True)
    name = models.CharField(max_length=200,unique=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    def category_tree(self):
        return " > ".join(str(x) for x in self.get_ancestors(False, True))
    category_tree.short_description = 'Category'
    class Meta:
        verbose_name_plural = "categories"
    class MPTTMeta:
        order_insertion_by = ['name']

class Type(models.Model):
    name = models.CharField(max_length=200)
    table = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name

class Currency(models.Model):
    long_name = models.CharField(max_length=200,null=True)
    short_name = models.CharField(max_length=3)
    locale = models.CharField(max_length=5, default='en_US')
    def __str__(self):
        return "({0}) {1}".format(self.short_name, self.long_name)
    class Meta:
        verbose_name_plural = "currencies"

class Account(models.Model):
    type = models.ForeignKey(Type)
    currency = models.ForeignKey(Currency)
    name = models.CharField(max_length=200, unique=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return "{0}: {1}({2})".format(self.name, self.type, self.currency.short_name)
    def save(self, *args, **kwargs):
        try:
            # New account
            if self.pk is None:
                Category.objects.get_or_create(name=TRANSFER_NAME.format(self.name),active=False)
            # Update account
            else:
                acc = Account.objects.get(pk=self.id)
                cat = Category.objects.get(name=TRANSFER_NAME.format(acc.name),active=False)
                if cat is not None:
                    cat.name = TRANSFER_NAME.format(self.name)
                    cat.save()
        except:
            e = sys.exc_info()[0]
            print "Error {0}".format(e)
        super(Account, self).save(*args, **kwargs)
    def delete(self):
        cat = Category.objects.get(name=TRANSFER_NAME.format(self.name))
        if cat is not None:
            cat.delete()
        super(Account, self).delete()

class Transaction(models.Model):
    category = models.ForeignKey(Category,null=True,blank=True,default=None)
    account = models.ForeignKey(Account)
    keywords = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateField(default=timezone.now)
    note = models.CharField(max_length=1000,null=True,blank=True)
    amount = models.DecimalField(max_digits=19,decimal_places=2)
    def formatted_amount(self):
        return Money(self.amount, self.account.currency.short_name).format(self.account.currency.locale, '$#,##0.00')
    formatted_amount.short_description = 'Amount'
    def __unicode__(self):
        return "Date: {0}, Category: {1}, Account: {2}, Amount: {3}, Keywords: '{4}', Note: '{5}'".format(self.date, "None" if self.category is None else self.category.name, self.account.name, self.formatted_amount(), self.keywords, self.note)
    def save(self, *args, **kwargs):
        try:
            if self.category.name.startswith("["):
                cat_name = self.category.name[13:-1]
                acc = Account.objects.get(name=cat_name)
                if acc is not None:
                    new_amount = self.amount * -1
                    word = " to " if new_amount < 0 else " from "
                    tran = Transaction(date=self.date, account=acc,amount=new_amount,note="Transfer {0} {1}".format(word, self.account.name), keywords="transfer")
                    word = " to " if word == " from " else " from "
                    self.category = None
                    self.note = "Transfer {0} {1}".format(word, acc.name)
                    self.keywords = "transfer"
                    tran.save()
        except:
            e = sys.exc_info()[0]
            print "Error {0}".format(e)
        super(Transaction, self).save(*args, **kwargs)


# ENUMS
class Days(enum.Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    labels = {
        MONDAY : 'Monday',
        TUESDAY : 'Tuesday',
        WEDNESDAY : 'Wednesday',
        THURSDAY : 'Thursday',
        FRIDAY : 'Friday',
        SATURDAY : 'Saturday',
        SUNDAY : 'Sunday'
    }

class Frequency(enum.Enum):
    DAILY = 1
    WEEKLY = 2
    BIWEEKLY = 3
    MONTHLY = 4
    YEARLY = 5

    labels = {
        DAILY : 'Daily',
        WEEKLY : 'Weekly',
        BIWEEKLY : 'Biweekly',
        MONTHLY : 'Monthly',
        YEARLY : 'Yearly'
    }

# Forms:
#gender = forms.TypedChoiceField(choices=GenderEnum.choices(), coerce=int)
# Model
#class Beer(models.Model):
    #style = enum.EnumField(BeerStyle, default=BeerStyle.LAGER)
#Beer.objects.create(style=BeerStyle.STOUT)
#Beer.objects.filter(style=BeerStyle.STOUT)


