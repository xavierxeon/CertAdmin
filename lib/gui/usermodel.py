#!/user/bin/env python3

import os
# pylint: disable=E0611
from PySide2.QtCore import Qt, QByteArray, QAbstractListModel
# pylint: enable=E0611

from ..settings import Settings
from ..usermanager import UserManager

class UserData:

    def __init__(self, name, active):

        self.name = name
        self.active = active

class UserModel(QAbstractListModel):

    RoleName = Qt.UserRole + 1
    RoleActive = Qt.UserRole + 2

    def __init__(self, settings):

        QAbstractListModel.__init__(self)
        self.settings = settings

        self._data = []
        self.load()

    def __del__(self):

        self._save()

    def roleNames(self):

        roles = {
            UserModel.RoleName: QByteArray(b'name')
            , UserModel.RoleActive: QByteArray(b'active')  
        }

        return roles

    def rowCount(self, index):

        rowCount = len(self._data)
        return rowCount

    def data(self, index, role):

        if not index.isValid():
            return None

        row = index.row()
        if row > len(self._data):
            return None

        data = self._data[row]
        if role == UserModel.RoleName:
            return data.name
        elif role == UserModel.RoleActive:
            return data.active
        
        return None

    def setData(self, index, value, role):

        if not index.isValid():
            return False

        row = index.row()
        if row > len(self._data):
            return False

        data = self._data[row]
        if role == UserModel.RoleActive:
            data.active = value
            return True
        
        return False

    def saveAndClear(self):

        self.beginResetModel()
        self._save()
        self._data.clear()
        self.endResetModel()    

    def load(self):

        self.beginResetModel()

        self._data.clear()

        certList = UserManager.readCertList(self.settings)
        userList = UserManager.readUserList(self.settings)
        
        for name in certList:
            self._data.append(UserData(name, name in userList))

        self.endResetModel()                

    def _save(self):

        userList = list()

        for userData in self._data:
            if not userData.active:
                continue
            userList.append(userData.name)

        UserManager.writeUserList(self.settings, userList)            
