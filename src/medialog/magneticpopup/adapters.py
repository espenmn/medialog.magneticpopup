# -*- coding: utf-8 -*-
from plone import api


class JavaScriptSettings(object):

    def __init__(self, context, request, field):
        self.request = request
        self.context = context
        self.image_size = self.get_size()
        self.popup_classes = self.get_classes()

    def get_size(self):
        try:
            return api.portal.get_registry_record('medialog.magneticpopup.interfaces.IMagneticPopupSettings.image_size')
        except:
            return 'large'

    def get_classes(self):
        try:
            return api.portal.get_registry_record('medialog.magneticpopup.interfaces.IMagneticPopupSettings.popup_classes')
        except:
            return 'img'

    def __call__(self):
        return {
            'data-popup-imagesize': self.image_size,
            'data-popup-imageclasses': self.popup_classes,
        }
