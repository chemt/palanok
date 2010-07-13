# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy  as _
from django.db.models import permalink

CURRENCY_CHOICES = ( 
        ('978', u'€'),
        ('840', u'$'),
        ('348', u'forint'),
        ('980', u'грн'),
    )

class Order(models.Model):
    title = models.CharField(_(u"Название счета"), max_length=200)
    email = models.EmailField(_(u"e-mail"))
    tel   = models.CharField(_(u"Телефон"), max_length=200)
    name  = models.CharField(_(u"Имя"), max_length=200)
    
    datetime = models.DateTimeField(_(u"Дата создания счета"), auto_now=True) 

    OrderID = models.CharField(_(u"OrderID"), max_length=200)

    amount  = models.PositiveIntegerField(_(u"Цена грн"), help_text=_(u"Цена в гривнах")) 
    amount2 = models.PositiveIntegerField(_(u"Цена2"), help_text=_(u"Цена в валютном эквиваленте"))
    
    PurchaseCurrency2 = models.CharField(_(u"Валюта"), help_text=_(u"Альтернативная валюта"), max_length=3, choices=CURRENCY_CHOICES) 
    
    OrderSignature = models.CharField(_(u"SHA-1"), max_length=200)
    AdditionalData = models.CharField(_(u"Дополнительные параметры"), max_length=200)
    
    IP = models.CharField(_(u"IP"), max_length=200)
    
    class Meta:
        ordering = ["-datetime", "OrderID"]
        verbose_name = _(u"Счет на оплату")
        verbose_name_plural = _(u"Счеты на оплату")
        
    class Admin(admin.ModelAdmin):
        list_display  = ('datetime', 'name', 'email', 'tel', 'OrderID', 'amount', 'amount2', 'PurchaseCurrency2')
        search_fields = ('OrderID', 'title', 'name', 'email', 'tel',)
        list_filter   = ('PurchaseCurrency2',)

        date_hierarchy = 'datetime'
        
        fieldsets = (
            (None,         {'fields': ('title', 'OrderID') } ),
            (_(u"Ціна"),   {'fields': ('amount', ('amount2', 'PurchaseCurrency2') ) } ),
            
            (_(u"Додатково"),         
                {
                    'fields': ('OrderSignature', 'AdditionalData', 'IP') , 
                    'classes': ('collapse',),
                }
            ),
        )

    def __unicode__(self):
        return u"%s" % self.title


class Platej(models.Model):
    title = models.CharField(_(u"Название платежа"), max_length=200)
    amount  = models.PositiveIntegerField(_(u"Цена грн"), help_text=_(u"Цена в гривнах")) 
    amount2 = models.PositiveIntegerField(_(u"Цена2"), help_text=_(u"Цена в валютном эквиваленте"))
    
    PurchaseCurrency2 = models.CharField(_(u"Валюта"), help_text=_(u"Альтернативная валюта"), max_length=3, choices=CURRENCY_CHOICES) 

    
    class Meta:
        verbose_name = _(u"Платеж")
        verbose_name_plural = _(u"Платежи")
        
    class Admin(admin.ModelAdmin):
        list_filter   = ('PurchaseCurrency2', )

    def __unicode__(self):
        return u"%s - %d" % (self.title, self.amount)
    
    @permalink
    def get_absolute_url(self):
        return ('pay_platej', [self.id])    


from cms.models import CMSPlugin
class PlatejPlugin(CMSPlugin):
    platej = models.ForeignKey(Platej)
    user_text = models.CharField(_(u"Текст ссылки"), max_length=200)

    display_uah = models.BooleanField(_(u"Отображать цену в UAH"), default=False)
    display_alt = models.BooleanField(_(u"Отображать цену в валюте"), default=False)
    ancor = models.BooleanField(_(u"Отображать ссылкой"), default=True)

    
    class Meta:
        verbose_name = _(u"Ссылка на платеж")
        verbose_name_plural = _(u"Ссылки на платежи")    

    def __unicode__(self):
        str = unicode(self.user_text)[:10] + r'/'
        if self.display_uah:
            str += u'%dгрн/' % self.platej.amount
        if self.display_alt:
            str += '(%d)/' % self.platej.amount2
        str += self.platej.title
        return str
        