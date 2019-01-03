#!/usr/bin/env python3

import os, binascii

from OpenSSL import crypto
from wapy.tools import Console
from .certbase import CertBase
from .settings import Settings

class CertCA(CertBase):

    
    def __init__(self, settings):

        CertBase.__init__(self, settings.getPrivateDir() + '/' + settings.getCAName())

    def create(self, serverName):

        self.key = self.generateNewKey()
        self.saveKey()

        serial = int(binascii.b2a_hex(os.urandom(8)), 16)
        newcert = self.generateCert(serverName, 0, serial)         

        newcert.set_issuer(newcert.get_subject())
        
        newcert.sign(self.key, CertBase.cryptAlgorithm)

        self.cert = newcert            
        self.saveCert()

    @staticmethod
    def loadOrCreate(settings):

        certCA = CertCA(settings)
        try:
            certCA.load()
        except CertBase.LoadError as e:
            print(Console.red(str(e)))
            message = 'type "{0}" to create the file (or anything else to quit): '.format(Console.yellow('create'))
            user = input(message)
            if 'create' != user:
                quit()        
            certCA.create(settings.getServerName())
            print(Console.green('created ca certificate'))  

        return certCA       
        