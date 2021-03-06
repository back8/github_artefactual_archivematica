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
# @subpackage archivematicaClientScript
# @author Joseph Perry <joseph@artefactual.com>

import uuid
from optparse import OptionParser
import sys
sys.path.append("/usr/lib/archivematica/archivematicaCommon")
from fileOperations import updateSizeAndChecksum
from fileOperations import addFileToSIP

def getOriginalFileUUID(SIPUUID, filePath):
    ret = fileUUID

def preservation():
    for file in files:
        
        #create an entry for the file
        fileUUID = uuid.uuid4().__str__()
        addFileToSIP(filePathRelativeToSIP, fileUUID, opts.sipUUID, opts.eventIdentifierUUID, opts.date, use=opts.use)
        updateSizeAndChecksum(opts.fileUUID, \
                     opts.filePath, \
                     opts.date, \
                     opts.eventIdentifierUUID)
        
        #move the file to the appropriate location + name
        
def createDipDirectoryIfNeeded():
    try:
        os.mkdir()
    except:
        return

def access():
    getOriginalFileUUID()
    moveToDIPDirectory 
    

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-i",  "--fileUUID",          action="store", dest="fileUUID", default="")
    parser.add_option("-p",  "--filePath",          action="store", dest="filePath", default="")
    parser.add_option("-d",  "--date",              action="store", dest="date", default="")
    parser.add_option("-u",  "--eventIdentifierUUID", action="store", dest="eventIdentifierUUID", default="")
    (opts, args) = parser.parse_args()

    updateSizeAndChecksum(opts.fileUUID, \
                     opts.filePath, \
                     opts.date, \
                     opts.eventIdentifierUUID)
