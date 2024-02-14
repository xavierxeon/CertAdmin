import QtQuick 
import QtQuick.Layouts 

Item
{
    height: 70

    ColumnLayout
    {
        anchors.fill: parent

        Text
        {
            text: "Server"
            font
            {
                bold: true
                pixelSize: 15
            }
        }

        Text
        {
            Layout.leftMargin: 10
            textFormat: Text.StyledText
            text: "<b>subject:</b> " + PyInterface.serverSubject
        }

        Text
        {
            Layout.leftMargin: 10
            textFormat: Text.StyledText
            text: "<b>issuer:</b>  " + PyInterface.serverIssuer
        }
    }         
}