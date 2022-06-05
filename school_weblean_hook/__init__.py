# from . import models
# from . import hook
from odoo.http import WebRequest
from odoo import SUPERUSER_ID, api

def _weblearns_pre_init_hook(cr):
    # cr.execute('''update res_partner set mobile = '123456789' where mobile is null''')
    # cr.commit()

    env = api.Environment(cr, SUPERUSER_ID, {})
    env['res.partner'].hello_hook()

def _weblearns_post_init_hook(cr, registry):
    cr.execute('''update res_partner set vat = 'vat123' where vat is null''')
    cr.commit()

def _weblearns_unistall_hook(cr, registry):
    cr.execute("update res_partner set vat = '' where vat ='vat123'")
    cr.commit()

def _weblearns_post_load_hook():
    monkey_patch_set_handle = WebRequest.set_handler

    def set_handle(self, endpoint, arguments, auth):
        monkey_patch_set_handle(self, endpoint, arguments, auth)

    WebRequest.set_handler = set_handle

    monkey_page_init = WebRequest.__init__

    def __init__(self, httprequest):
        monkey_page_init(self, httprequest)
        self.weblearns= "This is call from set handle method using monkey path"
        print(self.weblearns)

    WebRequest.__init__ = __init__
