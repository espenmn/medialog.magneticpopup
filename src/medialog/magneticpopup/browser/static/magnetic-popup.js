require([
    'jquery',
    '++plone++magneticpopup/jquery.magnific-popup-min'
], function($) {
   $('#content-core img').magnificPopup({
    type: 'image',
    callbacks: {
        elementParse: function(item) {
            item.src = item.el.attr('src');
        }
    }
    });
});
