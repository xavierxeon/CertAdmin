#!/usr/bin/env python3
 
from .certbase import CertBase
from .settings import Settings
from OpenSSL import crypto

class CertServer(CertBase):
    
    def __init__(self, settings, certCA):

        CertBase.__init__(self, settings.getPrivateDir() + '/server')
        self.certCA = certCA

    def create(self, serverName):

        self.key = self.generateNewKey()
        self.saveKey()

        newcert = self.generateCert(serverName, 2, 1)

        newcert.add_extensions([
            crypto.X509Extension(b'subjectKeyIdentifier', False, b'hash', subject = newcert),
            crypto.X509Extension(b'basicConstraints', False, b'CA:FALSE'),
            crypto.X509Extension(b'authorityKeyIdentifier', False, b'issuer:always', issuer=self.certCA.cert),
        ])        

        newcert.set_issuer(self.certCA.cert.get_subject())
        newcert.sign(self.certCA.key, self.crptAlgorithm)

        self.cert = newcert            
        self.saveCert()
