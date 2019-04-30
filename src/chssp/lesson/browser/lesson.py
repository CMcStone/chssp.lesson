from chssp.lesson import MessageFactory as _
from plone.supermodel import model
from zope import schema
from Acquisition import aq_inner
from plone import api
from Products.Five import BrowserView
from plone.dexterity.browser.view import DefaultView



class LessonView(BrowserView):
    """ The default view for lessons"""
    
    
