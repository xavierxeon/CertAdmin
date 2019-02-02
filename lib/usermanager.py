#!/usr/bin/env python3

# in /var/www/certs/passwd:
#/CN=test001:xxj31ZMTZzkVA

import os

from .settings import Settings

from xxpystuff.tools import Console

class UserManager:

    class UserError(Exception):

        pass 

    def __init__(self, settings):

        self.settings = settings
        self.userList = list()
        self.certList = list()

        self._load()

    def add(self, name):

        if not name in self.certList:
            raise UserManager.UserError(Console.red('no certificate for user {0}').format(name))

        if name in self.userList:
            raise UserManager.UserError(Console.cyan('user {0} has already access').format(name))

        self.userList.append(name)
        self._save()

    def remove(self, name):

        if not name in self.certList:
            raise UserManager.UserError(Console.red('no certificate for user {0}').format(name))

        if not name in self.userList:
            raise UserManager.UserError(Console.cyan('user {0} has no access').format(name))

        self.userList.remove(name)
        self._save()

    @staticmethod
    def readCertList(settings):

        certList = list()

        certPath = settings.getUserDir()
        for file in os.listdir(certPath):
            if not file.endswith('.p12'):
                continue
            name = file.replace('.p12', '')
            certList.append(name)


        certList.sort()
        return certList

    @staticmethod
    def readUserList(settings):

        userList = list()

        if not os.path.exists(settings.getPasswordFileName()):
            return userList

        with open(settings.getPasswordFileName(), 'r') as infile:
            for line in infile:
                line = line.replace('/CN=', '')
                name = line.replace(':xxj31ZMTZzkVA', '').rstrip()
                userList.append(name)

        userList.sort()
        return userList

    @staticmethod
    def writeUserList(settings, userList):

        userList.sort()
        with open(settings.getPasswordFileName(), 'w') as outfile:
            for user in userList:
                content = '/CN={0}:xxj31ZMTZzkVA\n'.format(user)
                outfile.write(content)
        

    def _load(self):

        self.certList = UserManager.readCertList(self.settings)
        self.userList = UserManager.readUserList(self.settings)
   
    def _save(self):

        UserManager.writeUserList(self.settings, self.userList)
