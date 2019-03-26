# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from chssp.lesson.testing import CHSSP_LESSON_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


no_get_installer = False


try:
    from Products.CMFPlone.utils import get_installer
except Exception:
    no_get_installer = True


class TestSetup(unittest.TestCase):
    """Test that chssp.lesson is properly installed."""

    layer = CHSSP_LESSON_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if chssp.lesson is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'chssp.lesson'))

    def test_browserlayer(self):
        """Test that IChsspLessonLayer is registered."""
        from chssp.lesson.interfaces import (
            IChsspLessonLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IChsspLessonLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CHSSP_LESSON_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['chssp.lesson'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if chssp.lesson is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'chssp.lesson'))

    def test_browserlayer_removed(self):
        """Test that IChsspLessonLayer is removed."""
        from chssp.lesson.interfaces import \
            IChsspLessonLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IChsspLessonLayer,
            utils.registered_layers())
