import QtQuick 
import QtQuick.Controls 
import QtQuick.Window 
import QtCore
import QtQuick.Layouts 

ApplicationWindow 
{
    id: applicationWindow
    title: "CertAdmin"
    visible: true

    function setFocusOnAdd()
    {
        addUser.focus = true;
    }

    Settings 
    {
        property alias x: applicationWindow.x
        property alias y: applicationWindow.y
        property alias width: applicationWindow.width
        property alias height: applicationWindow.height
    }

    ColumnLayout 
    {
        anchors.fill: parent

        CAInfo
        {
            Layout.fillWidth: true
        }

        Divider
        {
            Layout.fillWidth: true
        }


        AddServer
        {
            Layout.fillWidth: true
            Layout.margins: 10             
            visible: !PyInterface.serverAvailable
        }
        ServerInfo
        {
            Layout.fillWidth: true 
            visible: PyInterface.serverAvailable  
        }

        Divider
        {
            Layout.fillWidth: true
        }


        ClientHeader
        {
            Layout.fillWidth: true
        }
        AddUser
        {
            id: addUser

            Layout.fillWidth: true
            KeyNavigation.down: userList
        }
        UserList
        {
            id: userList

            Layout.fillWidth: true
            Layout.fillHeight: true
            focus: true
        }
    }
}