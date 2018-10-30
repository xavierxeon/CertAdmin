#!/usr/bin/env python3

import os
from OpenSSL import crypto

class CertBase:

    class LoadError(Exception):

        pass
        
    secondsPerDay = 24 * 60 + 60
    crptAlgorithm = 'sha256'
    

    def __init__(self, baseName):

        self._baseName = baseName

        self.cert = None
        self.key = None

    def load(self):

        try:
            with open(self._certFileName(), 'r') as certFile:
                self.cert = crypto.load_certificate(crypto.FILETYPE_PEM, certFile.read())
        except:
            raise CertBase.LoadError('unable to load cert file {0}'.format(self._certFileName()))

        try:
            with open(self._keyFileName(), 'r') as keyFile:
                self.key = crypto.load_privatekey(crypto.FILETYPE_PEM, keyFile.read())
        except:
            raise CertBase.LoadError('unable to load key file {0}'.format(self._keyFileName()))

    def saveCert(self):

        certContent = crypto.dump_certificate(crypto.FILETYPE_PEM, self.cert).decode()
        with open(self._certFileName(), 'w') as certFile:
            certFile.write(certContent)

    def saveKey(self, password = None):

        if not self.key:
            return

        keyContent = crypto.dump_privatekey(crypto.FILETYPE_PEM, self.key, passphrase = password).decode()
        with open(self._keyFileName(), 'w') as keyFile:
            keyFile.write(keyContent)

    def generateNewKey(self):

        newkey = crypto.PKey()
        newkey.generate_key(crypto.TYPE_RSA, 2048)

        return newkey

    def generateCert(self, commonName, version, serialNumber):

        newcert = crypto.X509()
        newcert.set_version(version)
        newcert.set_serial_number(serialNumber)
        newcert.set_pubkey(self.key)        

        newcert.gmtime_adj_notBefore(0)
        newcert.gmtime_adj_notAfter(10 * 365 * self.secondsPerDay)

        subj = newcert.get_subject()
        subj.commonName = commonName
        
        return newcert

    def _certFileName(self):

        return self._baseName + '.crt'

    def _keyFileName(self):
        
        return self._baseName + '.key'
        