#!/usr/bin/env python3

import os, json
from wapy.tools import Console, JSONSettings

class Settings(JSONSettings):

    _fileName = 'certadmin.json'
    _template = {
        'certdir': ''
        , 'names': {
            'server' : 'localhost'
            , 'ca': 'ca'
        }
    }

    def __init__(self):

        JSONSettings.__init__(self, self._fileName, self._template)

    def load(self):

        super().load()       

        os.makedirs(self.getPrivateDir(), exist_ok = True)
        os.makedirs(self.getUserDir(), exist_ok = True)


    def getPrivateDir(self):

        name = '{0}/private'.format(self._data['certdir'])
        return name

    def getUserDir(self):

        name = '{0}/users'.format(self._data['certdir'])
        return name        
    
    def getServerName(self):

        name = self._data['names']['server']
        return name

    def getCAName(self):

        name = self._data['names']['ca']
        return name

    def getPasswordFileName(self):

        name = '{0}/passwd'.format(self._data['certdir'])
        return name

