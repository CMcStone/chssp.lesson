# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import chssp.lesson


class ChsspLessonLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=chssp.lesson)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'chssp.lesson:default')


CHSSP_LESSON_FIXTURE = ChsspLessonLayer()


CHSSP_LESSON_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CHSSP_LESSON_FIXTURE,),
    name='ChsspLessonLayer:IntegrationTesting',
)


CHSSP_LESSON_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CHSSP_LESSON_FIXTURE,),
    name='ChsspLessonLayer:FunctionalTesting',
)


CHSSP_LESSON_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CHSSP_LESSON_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='ChsspLessonLayer:AcceptanceTesting',
)
