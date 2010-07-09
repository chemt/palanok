from dbgettext.registry import registry, Options
from models import PlatejPlugin

class PayOptions(Options):
    attributes = ('user_text',)
    parent = 'page'

registry.register(PlatejPlugin, PayOptions)