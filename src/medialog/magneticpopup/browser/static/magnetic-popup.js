require([
    'jquery',
    '++plone++magneticpopup/jquery.magnific-popup-min'
], function($) {
   $('#content-core img').magnificPopup({
    type: 'image',
    callbacks: {
        elementParse: function(item) {
            itemsrc = item.el.attr('src');
            try {
                item.src = itemsrc.split("/@@images")[0];
            }
            catch(err) {
    			item.src = itemsrc;
			}
        }
    }
    });
});
