# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from prima.theme.testing import PRIMA_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that prima.theme is properly installed."""

    layer = PRIMA_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if prima.theme is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('prima.theme'))

    def test_uninstall(self):
        """Test if prima.theme is cleanly uninstalled."""
        self.installer.uninstallProducts(['prima.theme'])
        self.assertFalse(self.installer.isProductInstalled('prima.theme'))

    def test_browserlayer(self):
        """Test that IPrimaThemeLayer is registered."""
        from prima.theme.interfaces import IPrimaThemeLayer
        from plone.browserlayer import utils
        self.assertIn(IPrimaThemeLayer, utils.registered_layers())
