#!/usr/bin/env python3
 
import random, string, json
from .certbase import CertBase
from .settings import Settings
from OpenSSL import crypto

class CertUser(CertBase):
    
    def __init__(self, settings, name, certCA):

        CertBase.__init__(self, settings.getUserDir() + '/' + name)
        self.userDir = settings.getUserDir()
        self.name = name
        self.certCA = certCA
        self.password = ''

        self.serial = 0
        self._readAndIncrememntSerial()

    def create(self):

        self._createPassword()
        req = self._createRequest()
        self.key = req.get_pubkey()
       
        newcert = self.generateCert(self.name, 2, self.serial)

        newcert.add_extensions([
            crypto.X509Extension(b'subjectKeyIdentifier', False, b'hash', subject = newcert),
            crypto.X509Extension(b'basicConstraints', False, b'CA:FALSE'),
            crypto.X509Extension(b'authorityKeyIdentifier', False, b'issuer:always', issuer=self.certCA.cert),
        ])
        
        newcert.set_issuer(self.certCA.cert.get_subject())
        newcert.sign(self.certCA.key, self.crptAlgorithm)

        self.cert = newcert            

        p12 = crypto.PKCS12()
        p12.set_privatekey(self.key)
        p12.set_certificate(self.cert)
        p12.set_friendlyname(self.name.encode())

        p12Content = p12.export(self.password.encode())
        p12FileName = '{0}/{1}.p12'.format(self.userDir, self.name)
        with open(p12FileName, 'wb') as p12File:
            p12File.write(p12Content)

    def _createPassword(self):

        for _ in range(20):
            self.password += random.choice(string.ascii_letters + string.digits)

        passwordFileName = '{0}/{1}_pwd.txt'.format(self.userDir, self.name)
        with open(passwordFileName, 'w') as passwordFile:
            passwordFile.write(self.password)
            passwordFile.write('\n')

    def _createRequest(self):

        reqkey = self.generateNewKey()

        req = crypto.X509Req()
        subj = req.get_subject()
        subj.commonName = self.name
        req.set_pubkey(reqkey)
        req.sign(reqkey, self.crptAlgorithm)

        return req

    def _readAndIncrememntSerial(self):

        serialFileName = self.userDir + '/.serial.json'
        data = {'serial' : 0}

        try:
            with open(serialFileName, 'r') as infile:
                data = json.load(infile)
                self.serial = data['serial']
        except FileNotFoundError:
            self.serial = 2

        data['serial'] = self.serial + 1
        with open(serialFileName, 'w') as outfile:
            json.dump(data, outfile)

