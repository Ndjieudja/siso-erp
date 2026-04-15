# --*-- encoding:utf8 --*--

from odoo import http
from odoo.http import request

from odoo import http
from odoo.http import request



class SisoPortfolio(http.Controller):


    @http.route('/portfolio', type='http', auth='public', website=True)
    def portfolio(self, **kwargs):
        testimonials = [
                {
                    'img': 'testimonial-1.jpg',
                    'name': 'Client 1',
                    'profession': 'Designer',
                    'text': 'Excellent service!',
                    'stars': 5
                },
                {
                    'img': 'testimonial-2.jpg',
                    'name': 'Client 2',
                    'profession': 'Developer',
                    'text': 'Highly recommended!',
                    'stars': 5
                },
                {
                    'img': 'testimonial-3.jpg',
                    'name': 'Client 3',
                    'profession': 'Manager',
                    'text': 'Very professional!',
                    'stars': 5
                },
            ]

        breadcrumbs = [
                {'name': 'Home', 'url': '/'},
                {'name': 'Portfolio', 'url': None},
            ]
        
        title = "mon porfolio"
        return request.render('siso_portfolio.siso_testimonial_page', {
            'testimonials': testimonials,
            'breadcrumbs': breadcrumbs,
            'title': title
        })
    
    @http.route('/about', type='http', auth='public', website=True)
    def about(self, **kwargs):
         return request.render('siso_portfolio.siso_about_page', {
        })
         
    @http.route('/services', type='http', auth='public', website=True)
    def services(self, **kwargs):
         return request.render('siso_portfolio.siso_services_page', {
        })
         
    @http.route('/contact', type='http', auth='public', website=True)
    def contact(self, **kwargs):
         return request.render('siso_portfolio.siso_contact_page', {
        })
         
    @http.route('/booking', type='http', auth='public', website=True)
    def booking(self, **kwargs):
         return request.render('siso_portfolio.siso_booking_page', {
        })
         
    @http.route('/team', type='http', auth='public', website=True)
    def technician(self, **kwargs):
         return request.render('siso_portfolio.siso_technician_page', {
        })
    
    @http.route('/appologie', type='http', auth='public', website=True)
    def appologie(self, **kwargs):
         return request.render('siso_portfolio.siso_appologie_page', {
        })