#!/usr/bin/python -OO

# This file is part of Archivematica.
#
# Copyright 2010-2013 Artefactual Systems Inc. <http://artefactual.com>
#
# Archivematica is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Archivematica is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Archivematica.  If not, see <http://www.gnu.org/licenses/>.

# @package Archivematica
# @subpackage MCPServer
# @author Joseph Perry <joseph@artefactual.com>

import databaseInterface
import threading
import uuid
import sys
import time
#select * from MicroServiceChainChoice JOIN MicroServiceChains on chainAvailable = MicroServiceChains.pk;
#| pk | choiceAvailableAtLink | chainAvailable | pk | startingLink | description

from linkTaskManager import linkTaskManager
from taskStandard import taskStandard
import jobChain
import databaseInterface
import lxml.etree as etree
import os
import archivematicaMCP
global choicesAvailableForUnits
choicesAvailableForUnits = {}
choicesAvailableForUnitsLock = threading.Lock()

class linkTaskManagerLoadMagicLink:
    """Load a link from the unit to process.
        Deprecated! Replaced with Set/Load Unit Variable"""
    def __init__(self, jobChainLink, pk, unit):
        self.pk = pk
        self.jobChainLink = jobChainLink
        self.UUID = uuid.uuid4().__str__()
        self.unit = unit

        ###Update the unit
        magicLink = self.unit.getMagicLink()
        if magicLink != None:
            link, exitStatus = magicLink
            self.jobChainLink.setExitMessage("Completed successfully")
            self.jobChainLink.jobChain.nextChainLink(link)
