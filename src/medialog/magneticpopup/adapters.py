# -*- coding: utf-8 -*-
from plone import api


class JavaScriptSettings(object):

    def __init__(self, context, request, field):
        self.request = request
        self.context = context
<<<<<<< HEAD
        #self.field = field
        #self.image_size = 'preview'
        self.image_size = self.get_size()

    def get_size(self):
        try:
            return api.portal.get_registry_record('medialog.magneticpopup.interfaces.IMagneticPopupSettings.image_size')
        finally:
            return 'large'
=======
        self.field = field
        self.image_size = api.portal.get_registry_record('medialog.magneticpopup.interfaces.IMagneticPopupSettings.image_size') 
        self.popup_classes = api.portal.get_registry_record('medialog.magneticpopup.interfaces.IMagneticPopupSettings.popup_classes') 
>>>>>>> origin/master

    def __call__(self):
        return {
<<<<<<< HEAD
            'data-popup-imagesize': self.image_size or None,
        }
=======
            'data-popup-imagesize': self.image_size,
            'data-popup-imageclasses': self.popup_classes,
        }
>>>>>>> origin/master
