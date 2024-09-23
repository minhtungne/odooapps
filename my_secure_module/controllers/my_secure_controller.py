from odoo import http

class MySecureModule(http.Controller):
    @http.route('/secure/home', type='http', auth='public', website=True)
    def home(self, **kw):
        return "This is Home Page"

    @http.route('/secure/next', type='http', auth='public', website=True)
    def next(self, **kw):
        return "This is Next Page"

    @http.route('/secure/previous', type='http', auth='public', website=True)
    def previous(self, **kw):
        return "This is Previous Page"

