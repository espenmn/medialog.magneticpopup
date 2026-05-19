(function ($) {
    'use strict';
    
    $(document).ready(function () {
        const el = document.querySelector('body');
        const image_size = el.getAttribute('data-popup-imagesize');
        const popup_classes = el.getAttribute('data-popup-imageclasses');

        $(popup_classes).magnificPopup({
            type: 'image',
            cursor: 'mfp-zoom-out-cur',
            mainClass: 'mfp-with-zoom',

            gallery: {
                enabled: true,
                navigateByImgClick: true,
                preload: [0, 1]
            },

            zoom: {
                enabled: true,
                duration: 200,
                easing: 'ease-in-out',

                opener: function (openerElement) {
                    return openerElement.is('img')
                        ? openerElement
                        : openerElement.find('img');
                }
            },

            callbacks: {
                elementParse: function (item) {

                    const itemsrc = item.el.attr('src');

                    try {
                        const image_url = itemsrc.split('/@@images')[0];

                        item.src =
                            image_url + '/@@images/image/' + image_size;

                    } catch (err) {
                        item.src = itemsrc;
                    }
                }
            }
        });

        $('.mfp-image-link').magnificPopup();

        $('.wall-of-images').each(function () {

            $(this).magnificPopup({
                delegate: 'img',
                type: 'image',

                opener: function (openerElement) {
                    return openerElement.is('img')
                        ? openerElement
                        : openerElement.find('img');
                },

                gallery: {
                    enabled: true
                },

                callbacks: {
                    elementParse: function (item) {

                        const itemsrc = item.el.attr('src');

                        try {
                            const image_url =
                                itemsrc.split('/@@images')[0];

                            item.src =
                                image_url + '/@@images/image/' + image_size;

                        } catch (err) {
                            item.src = itemsrc;
                        }
                    }
                }
            });
        });

    });

})(jQuery);