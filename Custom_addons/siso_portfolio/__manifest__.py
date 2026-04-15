{
    'name': "SISO Portfolio",
    'version': '1.0',
    'summary': "Module Portfolio Simple solution ets ",

    'description': """
        Ce module permet d'afficher des pages portfolio et témoignages
        en utilisant le template Plumberz et Owl Carousel.
    """,

    'author': "NDJIEUDJA Gabriel",
    'website': "https://ssolutionets.com",
    'category': 'Website',
    'depends': ['base', 'website'],

    'data': [
        # Templates QWeb
        'views/components/carousel.xml',
        'views/components/page_header.xml',
        'views/components/testimonial_card.xml',
        'views/layout.xml',
        'views/testimonial_page.xml',
        'views/about_page.xml',
        'views/services.xml',
        # 'views/contact.xml',
        
        # Données initiales si besoin
        # 'views/menu.xml',
        # 'views/website_templates.xml',
        # 'views/projects_views.xml',
        # 'data/siso_portfolio_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # CSS
            'siso_portfolio/static/css/bootstrap.min.css',
            'siso_portfolio/static/css/style.css',
            'siso_portfolio/static/lib/animate/animate.min.css',
            'siso_portfolio/static/lib/owlcarousel/assets/owl.carousel.min.css',
            'siso_portfolio/static/lib/tempusdominus/css/tempusdominus-bootstrap-4.min.css',

            # JS
            'siso_portfolio/static/lib/wow/wow.min.js',
            'siso_portfolio/static/lib/easing/easing.min.js',
            'siso_portfolio/static/lib/waypoints/waypoints.min.js',
            'siso_portfolio/static/lib/counterup/counterup.min.js',
            'siso_portfolio/static/lib/owlcarousel/owl.carousel.min.js',
            'siso_portfolio/static/lib/tempusdominus/js/moment.min.js',
            'siso_portfolio/static/lib/tempusdominus/js/moment-timezone.min.js',
            'siso_portfolio/static/lib/tempusdominus/js/tempusdominus-bootstrap-4.min.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}