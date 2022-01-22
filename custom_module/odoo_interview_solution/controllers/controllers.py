# -*- coding: utf-8 -*-
# from odoo import http


# class OdooInterviewSolution(http.Controller):
#     @http.route('/odoo_interview_solution/odoo_interview_solution/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_interview_solution/odoo_interview_solution/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_interview_solution.listing', {
#             'root': '/odoo_interview_solution/odoo_interview_solution',
#             'objects': http.request.env['odoo_interview_solution.odoo_interview_solution'].search([]),
#         })

#     @http.route('/odoo_interview_solution/odoo_interview_solution/objects/<model("odoo_interview_solution.odoo_interview_solution"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_interview_solution.object', {
#             'object': obj
#         })
