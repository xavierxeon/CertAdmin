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
            text: "Certificate Authority"
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
            text: "<b>subject:</b> " + PyInterface.caSubject
        }

        Text
        {
            Layout.leftMargin: 10
            textFormat: Text.StyledText
            text: "<b>issuer:</b>  " + PyInterface.caIssuer
        }
    }    
}