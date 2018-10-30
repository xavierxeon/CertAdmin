import QtQuick 2.11

Rectangle
{
    height: 30
    color: "#ffaaaa"
    border.color: "#ff0000"
    border.width: 5 

    MouseArea
    {
        anchors.fill: parent

        onClicked: PyInterface.createServer();
    }
    Text
    {
        anchors
        {
            horizontalCenter: parent.horizontalCenter
            verticalCenter: parent.verticalCenter  
        }

        text: "CLICK TO CREATE SERVER CERTIFICATE"
    }
}