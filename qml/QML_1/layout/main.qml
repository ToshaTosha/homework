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
        id: container
        anchors.fill:parent
        spacing:10

        RowLayout{
            id:header
            Layout.minimumHeight: win.height/9
            Layout.minimumWidth: parent.width
            Rect{
                ctext:"Header"
                Layout.fillWidth: true
                Layout.fillHeight: true
            }

        }
        RowLayout{
            id: content
            Layout.minimumHeight: (parent.height/9)*7-2*container.spacing
            Layout.minimumWidth: parent.width-2*container.spacing
            Layout.leftMargin: container.spacing
            Layout.rightMargin: container.spacing
            Rect{
                ctext:"Content"
                cborder:"lightgrey"
                ccolor:"white"
                Layout.fillHeight: true
                Layout.fillWidth: true
            }
        }
        RowLayout{
            id: footer
            Layout.minimumHeight: win.height/9
            spacing:5
            Rect{
                ctext:"1"
                Layout.minimumWidth: win.width/3
                Layout.fillHeight: true
            }
            Rect{
                ctext:"2"
                Layout.minimumWidth: win.width/3-2*footer.spacing
                Layout.fillHeight: true
            }
            Rect{
                ctext:"3"
                Layout.minimumWidth: win.width/3
                Layout.fillHeight: true
            }

        }
    }
}
