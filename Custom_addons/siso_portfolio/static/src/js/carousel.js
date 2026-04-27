/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.HeaderCarousel = publicWidget.Widget.extend({
    selector: '.header-carousel-home',

    start() {
        this.$el.owlCarousel({
            items: 1,
            loop: true,
            autoplay: true,
            autoplayTimeout: 3000,
            animateOut: 'fadeOut'
        });

        // 🔥 Animation uniquement après changement
        this.$el.on('changed.owl.carousel', () => {
            this.animateText();
        });

        return this._super(...arguments);
    },

    animateText() {
        const $active = this.$el.find('.owl-item.active');

        // reset uniquement les éléments du slide actif
        $active.find('.anim-text').css({
            opacity: 0,
            transform: 'translateX(100px)'
        });

        // animation progressive
        $active.find('.anim-text').each(function(i) {
            setTimeout(() => {
                $(this).css({
                    opacity: 1,
                    transform: 'translateX(0)'
                });
            }, i * 200);
        });
    }
});