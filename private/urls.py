from django.conf.urls.defaults import *
from views import create_order
from views import do_pay
from views import pay_platej
#from views import payment_responce, payment_result


urlpatterns = patterns('',
    url(r'^card/new/', create_order, name='create_order'),
    url(r'^do_pay', do_pay),
    url(r'^pay_platej/(?P<id>\d+)/$', pay_platej, name="pay_platej"),
#    url(r'^secure/responce/(?P<id>\d+)/$', payment_responce, name='payment_responce'),
#    url(r'^secure/noize', payment_result, name='payment_result'), 
)