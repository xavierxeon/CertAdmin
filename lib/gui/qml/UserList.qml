import QtQuick 2.11
import QtQuick.Layouts 1.11

FocusScope
{
    id: userListScope

    MouseArea 
    {
        anchors.fill: parent; 
        propagateComposedEvents: true

        onClicked: 
        {
            userListScope.focus = true;
            mouse.accepted = false;
        }
    }

    Component
    {
        id: highlighter

        Rectangle
        {
            width: applicationWindow.width
            height: 30

            color: "#dddddd"
        }
    }

    ListView
    {
        id: userListView
        anchors.fill: parent

        focus: true

        model: userModel
        delegate: UserListDelegate {}

        highlight: highlighter
    }
}