import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.12


Window {
    id: win
    width: 480
    height: 700
    visible: true
    title: qsTr("layout")

    ColumnLayout{
        anchors.fill:parent
        spacing:10

        RowLayout{
            Layout.maximumHeight: parent.height/9
            Layout.minimumWidth: parent.width
            Rect {
                ctext:"Header"
                Layout.fillWidth: true
                Layout.fillHeight: true
            }
        }
        RowLayout{
            id: content
            Layout.minimumHeight: (parent.height/300)
            Layout.minimumWidth: parent.width-2*10
            Layout.leftMargin: 10
            Layout.rightMargin: 10
            Rect {
                ctext:"content"
                cborder:"lightgrey"
                ccolor:"white"
                Layout.fillHeight: true
                Layout.fillWidth: true
            }
        }
        RowLayout{
            Layout.maximumHeight: parent.height/9
            Layout.minimumWidth: parent.width
            Rect{
                ctext:"1"
                Layout.minimumWidth: win.width/3
                Layout.fillHeight: true
                ccolor:"lightgrey"
            }
            Rect{
                ctext:"2"
                Layout.minimumWidth: win.width/3
                Layout.fillHeight: true
                ccolor:"lightgrey"
            }
            Rect{
                ctext:"3"
                Layout.minimumWidth: win.width/3
                Layout.fillHeight: true
                ccolor:"lightgrey"
            }
        }
    }
}
