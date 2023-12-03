import QtQuick 2.15

Item {
    property alias ccolor: rect.color
    property alias ctext: text.text
    property alias cborder:rect.border.color

    Rectangle {
        id:rect
        anchors.fill: parent
        color:"lightgrey"
        border.color:"white"
        Text{
            id: text
            anchors.centerIn: parent
        }
    }
}