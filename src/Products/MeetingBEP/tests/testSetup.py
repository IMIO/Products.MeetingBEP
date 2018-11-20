# -*- coding: utf-8 -*-
#
# File: testSetup.py
#
# Copyright (c) 2018 by Imio.be
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

from Products.MeetingBEP.tests.MeetingBEPTestCase import MeetingBEPTestCase
from Products.MeetingCommunes.tests.testSetup import testSetup as mcts
from Products.PloneMeeting.tests.PloneMeetingTestCase import pm_logger


class testSetup(MeetingBEPTestCase, mcts):
    ''' '''

    def test_pm_WorkflowsRemovedOnReinstall(self):
        """Bypass test as we do not control workflows, we use MeetingCommunes ones."""
        pm_logger.info("Bypassing test test_pm_WorkflowsRemovedOnReinstall")


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testSetup, prefix='test_'))
    return suite
