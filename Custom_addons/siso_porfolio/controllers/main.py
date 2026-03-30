# -*- coding: utf-8 -*-
####################################################################################
#
#    SISO WEB based on Odoo, Open Source Management Solution
#    Copyright (C) 2023 (<https://ssolutionets.com).
#    Martial MBE < gabrielndjieudja@gmail.com | gabrielndjieudja@ssolutionets.com >
#    See LICENSE file for full copyright and licensing details.
#
####################################################################################




from odoo import http
from odoo.http import request

# class SisoPortfolio(http.Controller):

#     @http.route('/portfolio', auth='public', website=True)
#     def portfolio(self, **kw):
#         projects = request.env['siso.project'].sudo().search([])
#         skills = request.env['siso.skill'].sudo().search([])

#         return request.render('siso_portfolio.portfolio_page', {
#             'projects': projects,
#             'skills': skills
#         })

#     @http.route('/portfolio/<int:project_id>', auth='public', website=True)
#     def project_detail(self, project_id):
#         project = request.env['siso.project'].sudo().browse(project_id)

#         return request.render('siso_portfolio.project_detail', {
#             'project': project
#         })

from odoo import http
from odoo.http import request

class SisoPortfolio(http.Controller):
    @http.route('/testimonial', type='http', auth='public', website=True)
    def testimonial(self, **kwargs):
        testimonials = [
            {'img':'testimonial-1.jpg','name':'Client 1','profession':'Designer','text':'Excellent service!','stars':5},
            {'img':'testimonial-2.jpg','name':'Client 2','profession':'Developer','text':'Highly recommended!','stars':5},
            {'img':'testimonial-3.jpg','name':'Client 3','profession':'Manager','text':'Very professional!','stars':5},
        ]
        return request.render('siso_portfolio.siso_testimonial_page', {'testimonials': testimonials})