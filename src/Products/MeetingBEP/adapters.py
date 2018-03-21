# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Copyright (c) 2007 by PloneGov
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#
# ------------------------------------------------------------------------------

from AccessControl import ClassSecurityInfo
from Globals import InitializeClass
from zope.interface import implements
from plone import api

from Products.PloneMeeting.interfaces import IMeetingCustom
from Products.PloneMeeting.interfaces import IMeetingItemCustom
from Products.MeetingCommunes.adapters import CustomMeeting
from Products.MeetingCommunes.adapters import CustomMeetingItem
from Products.MeetingCommunes.adapters import MeetingCommunesWorkflowActions
from Products.MeetingCommunes.adapters import MeetingCommunesWorkflowConditions
from Products.MeetingCommunes.adapters import MeetingItemCommunesWorkflowActions
from Products.MeetingCommunes.adapters import MeetingItemCommunesWorkflowConditions
from Products.MeetingBEP.config import HR_CONFIDENTIAL_GROUP_ID
from Products.MeetingBEP.interfaces import IMeetingBEPWorkflowActions
from Products.MeetingBEP.interfaces import IMeetingBEPWorkflowConditions
from Products.MeetingBEP.interfaces import IMeetingItemBEPWorkflowActions
from Products.MeetingBEP.interfaces import IMeetingItemBEPWorkflowConditions


class CustomBEPMeeting(CustomMeeting):
    '''Adapter that adapts a custom meeting implementing IMeeting to the interface IMeetingCustom.'''

    implements(IMeetingCustom)
    security = ClassSecurityInfo()

    def __init__(self, meeting):
        self.context = meeting


class CustomBEPMeetingItem(CustomMeetingItem):
    '''Adapter that adapts a custom meeting item implementing IMeetingItem to the interface IMeetingItemCustom.'''
    implements(IMeetingItemCustom)
    security = ClassSecurityInfo()

    def __init__(self, item):
        self.context = item

    def showObservations(self):
        """Restricted power observers may not view observations."""
        res = True
        item = self.getSelf()
        tool = api.portal.get_tool('portal_plonemeeting')
        cfg = tool.getMeetingConfig(item)
        # hide observations to restricted power observers
        if tool.isPowerObserverForCfg(cfg, isRestricted=True):
            res = False
        return res

    def isPrivacyViewable(self):
        """Not for restricted power observers if :
           - item is returned_to_proposing_group;
           - item.proposingGroup is HR_CONFIDENTIAL_GROUP_ID."""
        item = self.getSelf()
        tool = api.portal.get_tool('portal_plonemeeting')
        cfg = tool.getMeetingConfig(item)
        is_restricted_power_observer = tool.isPowerObserverForCfg(cfg, isRestricted=True)
        res = True
        if is_restricted_power_observer and \
           (item.getProposingGroup() == HR_CONFIDENTIAL_GROUP_ID or
                item.queryState() == 'returned_to_proposing_group'):
            res = False
        if res:
            res = item.isPrivacyViewable()
        return res


class MeetingBEPWorkflowActions(MeetingCommunesWorkflowActions):
    ''' '''

    implements(IMeetingBEPWorkflowActions)
    security = ClassSecurityInfo()


class MeetingBEPWorkflowConditions(MeetingCommunesWorkflowConditions):
    ''' '''

    implements(IMeetingBEPWorkflowConditions)
    security = ClassSecurityInfo()


class MeetingItemBEPWorkflowActions(MeetingItemCommunesWorkflowActions):
    ''' '''

    implements(IMeetingItemBEPWorkflowActions)
    security = ClassSecurityInfo()


class MeetingItemBEPWorkflowConditions(MeetingItemCommunesWorkflowConditions):
    ''' '''

    implements(IMeetingItemBEPWorkflowConditions)
    security = ClassSecurityInfo()

    def __init__(self, item):
        self.context = item  # Implements IMeetingItem


# ------------------------------------------------------------------------------
InitializeClass(CustomBEPMeeting)
InitializeClass(CustomBEPMeetingItem)
InitializeClass(MeetingBEPWorkflowActions)
InitializeClass(MeetingBEPWorkflowConditions)
InitializeClass(MeetingItemBEPWorkflowActions)
InitializeClass(MeetingItemBEPWorkflowConditions)
# ------------------------------------------------------------------------------
