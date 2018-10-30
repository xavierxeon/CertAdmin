import QtQuick 2.11
import QtQuick.Layouts 1.11
import QtQuick.Controls 1.4

Item
{
    width: applicationWindow.width
    height: 30

    MouseArea 
    {
        anchors.fill: parent
        propagateComposedEvents: true

        onClicked: 
        {
            userListView.currentIndex = index            
            mouse.accepted = false
        }
    }    
    
    RowLayout
    {
        anchors.fill: parent

        Switch
        {
            id: activeSwitch
            Layout.leftMargin: 10

            checked: model.active

            onClicked: model.active = checked;

            MouseArea
            {
                anchors.fill: parent
                onClicked: 
                {
                    var newState = !activeSwitch.checked
                    activeSwitch.checked = newState
                    model.active = newState
                }
            }
        }
        Text
        {
            text: model.name

            Layout.fillWidth: true
        }
    }

    Keys.onPressed: 
    {
        if (event.key == Qt.Key_Left) 
        {
            model.active = false;
            activeSwitch.checked = false;
            event.accepted = true;
        }
        else if (event.key == Qt.Key_Right) 
        {
            model.active = true;
            activeSwitch.checked = true;
            event.accepted = true;
        }
        else if(event.key == Qt.Key_A)
        {
            applicationWindow.setFocusOnAdd();
            event.accepted = true;
        }
    }
}