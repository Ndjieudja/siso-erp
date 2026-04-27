/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.ServiceCarousel = publicWidget.Widget.extend({
    selector: ".service-carousel",

    start() {
        if (this.$el.length) {
            this.$el.owlCarousel({
                loop: true,
                margin: 20,
                nav: true,
                autoplay: true,
                autoplayTimeout: 3000,
                autoplayHoverPause: true,
                responsive: {
                    0: { items: 1 },
                    768: { items: 2 },
                    992: { items: 3 }
                }
            });
        }
        return this._super(...arguments);
    },
});