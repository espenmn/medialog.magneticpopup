require([
    'jquery',
    '++plone++magneticpopup/jquery.magnific-popup-min'
], function($) {
   $('img.image-inline, img.image-left, img.image-right, .wall-of-images img').magnificPopup({
    type: 'image',
    cursor: 'mfp-zoom-out-cur', 
    mainClass: 'mfp-with-zoom', 
    gallery: {
			enabled: true,
			navigateByImgClick: true,
			preload: [0,1] // Will preload 0 - before current, and 1 after the current image
	},
    zoom: {
    enabled: true, // By default it's false, so don't forget to enable it
    duration: 200, // duration of the effect, in milliseconds
    easing: 'ease-in-out', // CSS transition easing function
    opener: function(openerElement) {
      return openerElement.is('img') ? openerElement : openerElement.find('img');
       }
    },
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
