# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface

class ILesson(Interface):
    """Marker interface used for lesson objects"""


class IChsspLessonLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
