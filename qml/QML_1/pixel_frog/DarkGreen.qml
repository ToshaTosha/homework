import QtQuick 2.15

Item {
    property alias comColor: rect.color
    Rectangle{
        id:rect
        anchors.fill: parent
        color: "#086e0f";
    }
}
