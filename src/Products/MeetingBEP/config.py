# -*- coding: utf-8 -*-
#
# File: config.py
#
# Copyright (c) 2018 by Imio.be
#
# GNU General Public License (GPL)
#

from Products.CMFCore.permissions import setDefaultRoles

__author__ = """Gauthier Bastien <g.bastien@imio.be>, Andre NUYENS <a.nuyens@imio.be>"""
__docformat__ = 'plaintext'

PROJECTNAME = "MeetingBEP"

# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner', 'Contributor'))
product_globals = globals()
