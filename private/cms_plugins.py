# -*- coding: utf-8 -*-

from django.contrib import admin
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from models import PlatejPlugin

class LinkPayPlugin(CMSPluginBase):
    model = PlatejPlugin
    name = _(u"Платеж")
    
    text_enabled = True    
    render_template = "plugins/link_pay.html"
    
    def icon_src(self, instance):
        return settings.MEDIA_URL + u"img/small_visa.png"
    
    def render(self, context, instance, placeholder):
        context.update({
            'body': instance.user_text,
            'object': instance,
            'placeholder': placeholder
        })
        return context        


plugin_pool.register_plugin(LinkPayPlugin)
