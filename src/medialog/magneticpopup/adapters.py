# -*- coding: utf-8 -*-
from plone import api


class JavaScriptSettings(object):

    def __init__(self, context, request, field):
        self.request = request
        self.context = context
        self.field = field
        self.image_size = api.portal.get_registry_record('medialog.magneticpopup.interfaces.IMagneticPopupSettings.image_size') 

        
    def __call__(self):
        return {
            'data-popup-imagesize': self.image_size,
        }