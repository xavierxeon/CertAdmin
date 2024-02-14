import QtQuick 
import QtQuick.Layouts 

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