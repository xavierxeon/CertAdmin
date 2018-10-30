import QtQuick 2.11
import QtQuick.Layouts 1.11

FocusScope
{
    id: addUserView

    width: applicationWindow.width
    height: 30

    function addUser()
    {
        var userName = newUserName.text;
        newUserName.text = ""

        PyInterface.addUser(userName)
    }

    Rectangle
    {
        color: "#cccccc"
        anchors.fill: parent


        RowLayout
        {
            anchors.fill: parent

            Text
            {
                Layout.leftMargin: 10

                text: "Add user"
            }

            Rectangle
            {
                Layout.fillWidth: true
                Layout.fillHeight: true

                color: "#ffffff"
                border.color: "#cccccc"
                border.width: 5 

                TextInput 
                {
                    id: newUserName
                    focus: true

                    anchors.verticalCenter: parent.verticalCenter 
                    width: parent.width
                    x: 10

                    onAccepted: addUser()
                }
            }

            Text
            {
                Layout.rightMargin: 10

                text: "+"

                MouseArea
                {
                    anchors.fill: parent
                    onClicked: addUserView.addUser()
                }
            }
        }    
    }
}
