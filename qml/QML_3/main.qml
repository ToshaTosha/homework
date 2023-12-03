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
                id: header
                ctext:"Header"
                Layout.fillWidth: true
                Layout.fillHeight: true
            }
        }
        RowLayout{
            Layout.minimumHeight: (parent.height/300)
            Layout.minimumWidth: parent.width-2*10
            Layout.leftMargin: 10
            Layout.rightMargin: 10
            Rect {
                id:content
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
                id:btn1
                ctext:"1"
                Layout.minimumWidth: win.width/3
                Layout.fillHeight: true
                ccolor:"lightgrey"
                MouseArea{
                    anchors.fill:parent
                    onClicked:{
                        btn1.opacity=1
                        content.ctext="Item 1 content"
                        header.ctext="Header 1"
                        btn2.opacity=0.5
                        btn3.opacity=0.5
                    }
                }
            }
            Rect{
                id:btn2
                ctext:"2"
                Layout.minimumWidth: win.width/3
                Layout.fillHeight: true
                ccolor:"lightgrey"
                MouseArea{
                    anchors.fill:parent
                    onClicked:{
                        btn2.opacity=1
                        content.ctext="Item 2 content"
                        header.ctext="Header 2"
                        btn1.opacity=0.5
                        btn3.opacity=0.5
                    }
                }
            }
            Rect{
                id:btn3
                ctext:"3"
                Layout.minimumWidth: win.width/3
                Layout.fillHeight: true
                ccolor:"lightgrey"
                MouseArea{
                    anchors.fill:parent
                    onClicked:{
                        btn3.opacity=1
                        content.ctext="Item 3 content"
                        header.ctext="Header 3"
                        btn1.opacity=0.5
                        btn2.opacity=0.5
                    }
                }
            }
        }
    }
}
