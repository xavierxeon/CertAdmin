import QtQuick 2.11
import QtQuick.Controls 2.1

Image
{
    id: helpView

    //sourceSize.width: 30
    //sourceSize.height: 30    

    source: "Help.svg"

    function compileHelpText()
    {
        var content = "<h2>Keyboard Navigation</h2>";
        content += "<br>";

        content += "the list of clients has the focus when starting the gui"
        content += "<br>";

        content += "<p>";
        content += "<h3>in client list</h3>";
        content += "<br>";
        content += "<ul>";
        content += "<li><b>Up</b>: switch users</li>";
        content += "<li><b>Down</b>: switch users</li>";
        content += "<li><b>Left</b>: disable users</li>";
        content += "<li><b>Right</b>: enable users</li>";
        content += "<li><b>A</b>: focus add user</li>";
        content += "</ul>";
        content += "</p>";
    
        content += "<p>";
        content += "<h3>in add user</h3>";
        content += "<br>";
        content += "<ul>";
        content += "<li><b>Down</b>: focus user list</li>";
        content += "<li><b>Return</b>: add user</li>";
        content += "</ul>";
        content += "</p>";

        content += "for more help try the README file";


        return content;
    }

    MouseArea
    {
        anchors.fill: parent
        onClicked: helpPopup.open();        
    }

    Popup
    {
        id: helpPopup

        x: -helpView.x
        y: 0
        width: applicationWindow.width
        modal: true
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent        

        Text
        {
            anchors.fill: parent

            textFormat: Text.StyledText
            text: helpView.compileHelpText()            
        }
    }
}
