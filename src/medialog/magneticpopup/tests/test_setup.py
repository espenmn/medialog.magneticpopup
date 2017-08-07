# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from medialog.magneticpopup.testing import MEDIALOG_MAGNETICPOPUP_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that medialog.magneticpopup is properly installed."""

    layer = MEDIALOG_MAGNETICPOPUP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if medialog.magneticpopup is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'medialog.magneticpopup'))

    def test_browserlayer(self):
        """Test that IMedialogMagneticpopupLayer is registered."""
        from medialog.magneticpopup.interfaces import (
            IMedialogMagneticpopupLayer)
        from plone.browserlayer import utils
        self.assertIn(IMedialogMagneticpopupLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MEDIALOG_MAGNETICPOPUP_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['medialog.magneticpopup'])

    def test_product_uninstalled(self):
        """Test if medialog.magneticpopup is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'medialog.magneticpopup'))

    def test_browserlayer_removed(self):
        """Test that IMedialogMagneticpopupLayer is removed."""
        from medialog.magneticpopup.interfaces import \
            IMedialogMagneticpopupLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMedialogMagneticpopupLayer, utils.registered_layers())
