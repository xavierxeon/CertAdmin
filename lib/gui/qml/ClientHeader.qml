import QtQuick 2.11
import QtQuick.Layouts 1.11

Item
{
    height: 30

    RowLayout
    {
        anchors.fill: parent

        Text
        {
            Layout.fillWidth: true

            text: "Clients"
            
            font
            {
                bold: true
                pixelSize: 15
            }
        }      
        HelpView
        {

        }

    }
}