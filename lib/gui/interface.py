#!/usr/bin/env python3

from PySide6.QtCore import Qt, QObject, Slot, Property, Signal


from ..usermanager import UserManager
from ..certuser import CertUser
from ..certbase import CertBase
from ..certserver import CertServer
from .usermodel import UserModel


class Interface(QObject):

   signalServerCertAvailable = Signal()
   signalDummy = Signal()

   def __init__(self, settings, certCA, usermodel):

      QObject.__init__(self)
      self.settings = settings
      self.certCA = certCA

      self.certServer = CertServer(self.settings, self.certCA)
      try:
         self.certServer.load()
      except CertBase.LoadError:
         self.certServer = None

      self.usermodel = usermodel

   @Slot(None, result=None)
   def createServer(self):

      certServer = CertServer(self.settings, self.certCA)

      try:
         certServer.load()
         return
      except CertBase.LoadError:
         certServer.create(self.settings.getServerName())
         self.certServer = certServer

      self.signalServerCertAvailable.emit()

   @Slot(str, result=None)
   def addUser(self, name):

      self.usermodel.saveAndClear()

      certUser = CertUser(self.settings, name, self.certCA)
      try:
         certUser.load()
      except CertBase.LoadError:  # only if user does not exist
         certUser.create()
         try:
            userManager = UserManager(self.settings)
            userManager.add(name)
         except UserManager.UserError:
            pass

      self.usermodel.load()

   def _parseX509Name(self, x509Name):

      data = x509Name.get_components()
      content = ''
      for entry in data:
         if content:
            content += ', '
         content += '/{0}={1}'.format(entry[0].decode(), entry[1].decode())
      return content

   def _getCASubject(self):

      cert = self.certCA.cert
      return self._parseX509Name(cert.get_subject())

   def _getCAIssuer(self):

      cert = self.certCA.cert
      return self._parseX509Name(cert.get_issuer())

   def _getServerSubject(self):

      content = 'N/A'
      if self.certServer:
         cert = self.certServer.cert
         content = self._parseX509Name(cert.get_subject())

      return content

   def _getServerIssuer(self):

      content = 'N/A'
      if self.certServer:
         cert = self.certServer.cert
         content = self._parseX509Name(cert.get_issuer())

      return content

   def _getServerAvailable(self):

      if self.certServer:
         return True
      else:
         return False

   # properties
   caSubject = Property(str, _getCASubject, notify=signalDummy)
   caIssuer = Property(str, _getCAIssuer, notify=signalDummy)

   serverSubject = Property(str, _getServerSubject, notify=signalServerCertAvailable)
   serverIssuer = Property(str, _getServerIssuer, notify=signalServerCertAvailable)
   serverAvailable = Property(bool, _getServerAvailable, notify=signalServerCertAvailable)
