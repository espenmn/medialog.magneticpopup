require([
    'jquery',
    '++plone++magneticpopup/jquery.magnific-popup-min'
], function($) {
   $('img.image-popup, figure img, img.image-inline, img.image-left, img.image-right').magnificPopup({
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
                image_url = itemsrc.split('/@@images')[0];
                item.src =  image_url + '/@@images/image';
            }
            catch(err) {
    			item.src = itemsrc;
			}
        }
    }
    });
    $('.mfp-image-link').magnificPopup();
    $('.wall-of-images').each(function() { // the containers for all your galleries
    	$(this).magnificPopup({
        	delegate: 'img', // the selector for gallery item
        	type: 'image',
        	opener: function(openerElement) {
      			return openerElement.is('img') ? openerElement : openerElement.find('img');
       		},
        	gallery: {
        	  enabled:true
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
});
