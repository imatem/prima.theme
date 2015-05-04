# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.testing import z2
from zope.configuration import xmlconfig

import prima.theme


class PrimaThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            prima.theme,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'prima.theme:default')


PRIMA_THEME_FIXTURE = PrimaThemeLayer()


PRIMA_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PRIMA_THEME_FIXTURE,),
    name='PrimaThemeLayer:IntegrationTesting'
)


PRIMA_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PRIMA_THEME_FIXTURE,),
    name='PrimaThemeLayer:FunctionalTesting'
)


PRIMA_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PRIMA_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PrimaThemeLayer:AcceptanceTesting'
)
