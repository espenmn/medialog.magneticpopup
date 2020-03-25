# -*- coding: utf-8 -*-
# Default ENCODING = 'UTF-8'
"""Module where all interfaces, events and exceptions live."""


from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from z3c.form import interfaces
from zope import schema
from zope.interface import alsoProvides
from plone.supermodel import model


from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.magneticpopup')

class IMedialogMagneticpopupLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IMagneticPopupSettings(model.Schema):
    """Adds settings to medialog.controlpanel
    """

    model.fieldset(
        'popup',
        label=_(u'Popup settings'),
        fields=[
             'image_size',
             'popup_classes'
        ],
     )

    popup_classes = schema.Text(
        title = _("label_popup_classes", default=u"Popup image classes"),
        description = _("help_popupclasses",
                      default="Popup Image Classes"),
        default=u"img.image-popup, figure img, img.image-inline, img.image-left, img.image-right",
    )

    image_size = schema.Choice(
        title = _("label_imagesize", default=u"Image Size"),
        description = _("help_imagesize",
                      default="Popup Image Size"),
        vocabulary='plone.app.vocabularies.ImagesScales',
        default='large',
    )

alsoProvides(IMagneticPopupSettings, IMedialogControlpanelSettingsProvider)
