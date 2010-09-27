# -*- coding: utf-8 -*-
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from base64 import b64encode
import sha
import datetime
import merchant

from models import Order, Platej
from forms import PayForm
from django.template.context import RequestContext

dig12 = lambda(i): '%.12d' % i # format string to 12 chars with leading zero

def create_order(request, email, tel, name, amount, amount2, PurchaseCurrency2):
    PurchaseAmt       = dig12(amount * 100) 
    PurchaseCurrency  = '980' # UAH
    PurchaseAmt2      = dig12(amount2 * 100) 
    PurchaseCurrencyExponent = '2'
    time = datetime.datetime.now().isoformat()
    OrderID = 'Palanok_' + time
    AdditionalData = ''


    Signature = merchant.Password + merchant.MerID + merchant.AcqID + OrderID + PurchaseAmt + PurchaseCurrency + PurchaseAmt2 + PurchaseCurrency2 + AdditionalData
    Signature = b64encode(sha.new(Signature).digest())
    
    order = Order(
        email=email,
        tel=tel,
        name=name,
        OrderID=OrderID,
        amount=amount, 
        amount2=amount2, 
        PurchaseCurrency2=PurchaseCurrency2,
        OrderSignature=Signature,
        AdditionalData=AdditionalData,
        IP=request.META['REMOTE_ADDR']
    )
    
    order.save()
    
    MerRespURL  = 'https://www.verification.privatbank.ua/SENTRY/PaymentGateway/Application/wfrmresponse.aspx'
    # MerRespURL2 = r'http://hotelpalanok.com/secure/noize'
    # <input id='MerRespURL2' type='hidden' value='%(MerRespURL2)s'  name='MerRespURL2'>

    
    
    
    SignatureMethod = 'SHA1'
    form = """
    <body>
<FORM id='checkout' name='checkout' method=post action='https://www.verification.privatbank.ua/SENTRY/PaymentGateway/Application/CheckOutPage/CheckoutPage.aspx';>
    <input id='Version' type='hidden' name='Version' value='1.0.0'>
    <input id='MerID' type='hidden' value='%(MerID)s' name='MerID'>
    <input id='AcqID' type='hidden' value='%(AcqID)s' name='AcqID'>
    <input id='MerRespURL' type='hidden' value='%(MerRespURL)s'  name='MerRespURL'>
    <input id='PurchaseAmt' type='hidden' value='%(PurchaseAmt)s' name='PurchaseAmt'>
    <input id='PurchaseCurrency' type='hidden' value='%(PurchaseCurrency)s' name='PurchaseCurrency'>
    <input id='PurchaseAmt2' type='hidden' value='%(PurchaseAmt2)s' name='PurchaseAmt2'>
    <input id='PurchaseCurrency2' type='hidden' value='%(PurchaseCurrency2)s' name='PurchaseCurrency2'>
    <input id='PurchaseCurrencyExponent' type='hidden' value='2' name='PurchaseCurrencyExponent'>
    <input id='OrderID' type='hidden' value='%(OrderID)s' name='OrderID'>
    <input id='SignatureMethod' type='hidden' value='%(SignatureMethod)s' name='SignatureMethod'>
    <input id='Signature' type='hidden' value ='%(Signature)s' name='Signature'>
    <input id='CaptureFlag' type='hidden' value='A' name='CaptureFlag'>
<script>
document.getElementById('checkout').submit();
</script>
</FORM>
</body>
""" % dict(
    PurchaseAmt       = PurchaseAmt,
    PurchaseCurrency  = PurchaseCurrency,
    PurchaseAmt2      = PurchaseAmt2,
    PurchaseCurrency2 = PurchaseCurrency2,
    PurchaseCurrencyExponent = PurchaseCurrencyExponent,
    AdditionalData = AdditionalData,
    MerID   = merchant.MerID,
    AcqID   = merchant.AcqID,
    OrderID = OrderID,
    MerRespURL  = MerRespURL,
    #MerRespURL2 = MerRespURL2,
    Signature   = Signature,
    SignatureMethod = SignatureMethod
)

    return HttpResponse(form)



def do_pay(request):
    return create_order(request, 'Test pay', 80, 99, '980')


def pay_platej(request, id):
    platej = get_object_or_404(Platej, id=id)
    
    if request.method == 'POST':
        form = PayForm(request.POST)
        if form.is_valid():
            return create_order(
                request = request,
                name  = form.cleaned_data['name'],
                tel   = form.cleaned_data['tel'],
                email = form.cleaned_data['email'],
                amount  = platej.amount,
                amount2 = platej.amount2,
                PurchaseCurrency2 = platej.PurchaseCurrency2,
            )
    else:
        form = PayForm()
    
    c = RequestContext(request, dict(form=form, platej=platej))
    return render_to_response('pay_form.html', c)
