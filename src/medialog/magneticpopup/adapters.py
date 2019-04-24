# -*- coding: utf-8 -*-
from plone import api


class JavaScriptSettings(object):

    def __init__(self, context, request, field):
        self.request = request
        self.context = context
        #self.field = field
        #self.image_size = 'preview'
        self.image_size = self.get_size()

    def get_size(self):
        try:
            return api.portal.get_registry_record('medialog.magneticpopup.interfaces.IMagneticPopupSettings.image_size')
        finally:
            return 'large'

    def __call__(self):
        return {
            'data-popup-imagesize': self.image_size or None,
        }
