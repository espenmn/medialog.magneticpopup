# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from zope.interface import noLongerProvides, alsoProvides
from medialog.magneticpopup.interfaces import IMagneticPopupSettings
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'medialog.magneticpopup:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    alsoProvides(IMagneticPopupSettings, IMedialogControlpanelSettingsProvider)


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
    noLongerProvides(IMagneticPopupSettings, IMedialogControlpanelSettingsProvider)
