import QtQuick 2.15

Item {
    property alias comColor: rect.color
    Rectangle{
        id:rect
        width: 10 * 3
        height: 10 * 3
        anchors.fill: parent
        color: "#fff";
    }
}
