import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.12


Window {
    id: win
    width: 480
    height: 700
    visible: true
    title: qsTr("layout")

    property int dur: 500

    ColumnLayout{
        id: layout
        anchors.fill:parent
        spacing:10

        states:[
            State{
                name:"start"
                PropertyChanges {
                    target: btn1
                    opacity: 1;
                }
                PropertyChanges {
                    target: btn2
                    opacity: 1;
                }
                PropertyChanges {
                    target: btn3
                    opacity: 1;
                }
                PropertyChanges {
                    target: back
                    visible: false;
                }
                PropertyChanges {
                    target: header
                    ctext: "Header";
                    Layout.fillWidth: true;
                }
                PropertyChanges {
                    target: content
                    ctext: "Content";
                }
            },
            State{
                name:"item1"
                PropertyChanges {
                    target: btn1
                    opacity: 1;
                }
                PropertyChanges {
                    target: btn2
                    opacity: 0.5;
                }
                PropertyChanges {
                    target: btn3
                    opacity: 0.5;
                }
                PropertyChanges {
                    target: back
                    visible: true;
                }
                PropertyChanges {
                    target: header
                    ctext: "Header 1";
                }
                PropertyChanges {
                    target: content
                    ctext: "Item 1 content";
                }
            },
            State{
                name:"item2"
                PropertyChanges {
                    target:btn1
                    opacity: 0.5;
                }
                PropertyChanges {
                    target: btn2
                    opacity: 1;
                }
                PropertyChanges {
                    target: btn3
                    opacity: 0.5;
                }
                PropertyChanges {
                    target: back
                    visible: true;
                }
                PropertyChanges {
                    target: header
                    ctext: "Header 2";
                }
                PropertyChanges {
                    target: content
                    ctext: "Item 2 content";
                }
            },
            State{
                name:"item3"
                PropertyChanges {
                    target: btn1
                    opacity: 0.5;
                }
                PropertyChanges {
                    target: btn2
                    opacity: 0.5;
                }
                PropertyChanges {
                    target: btn3
                    opacity: 1;
                }
                PropertyChanges {
                    target: back
                    visible: true;
                }
                PropertyChanges {
                    target: header
                    ctext: "Header 3";
                }
                PropertyChanges {
                    target: content
                    ctext: "Item 3 content";
                }
            }
        ]

        state:"start"

        transitions:[
            Transition {
                from: "start"
                to: "item1"
                PropertyAnimation{targets: [btn1, btn2, btn3]; properties: "opacity"; duration:dur}
            },
            Transition {
                from: "item2"
                to: "item1"
                PropertyAnimation{targets: [btn1, btn2, btn3]; properties: "opacity"; duration:dur}
            },
            Transition {
                from: "item3"
                to: "item1"
                PropertyAnimation{targets: [btn1, btn2, btn3]; properties: "opacity"; duration:dur}
            },
            Transition {
                from: "start"
                to: "item2"
                PropertyAnimation{targets: [btn1, btn2, btn3]; properties: "opacity"; duration:dur}
            },
            Transition {
                from: "item1"
                to: "item2"
                PropertyAnimation{targets: [btn1, btn2, btn3]; properties: "opacity"; duration:dur}
            },
            Transition {
                from: "item3"
                to: "item2"
                PropertyAnimation{targets: [btn1, btn2, btn3]; properties: "opacity"; duration:dur}
            },
            Transition {
                from: "start"
                to: "item3"
                PropertyAnimation{targets: [btn1, btn2, btn3]; properties: "opacity"; duration:dur}
            },
            Transition {
                from: "item1"
                to: "item3"
                PropertyAnimation{targets: [btn1, btn2, btn3]; properties: "opacity"; duration:dur}
            },
            Transition {
                from: "item2"
                to: "item3"
                PropertyAnimation{targets: [btn1, btn2, btn3]; properties: "opacity"; duration:dur}
            },
            Transition {
                from: "item1"
                to: "start"
                PropertyAnimation{targets: [btn1, btn2, btn3]; properties: "opacity"; duration:dur}
            },
            Transition {
                from: "item2"
                to: "start"
                PropertyAnimation{targets: [btn1, btn2, btn3]; properties: "opacity"; duration:dur}
            },
            Transition {
                from: "item3"
                to: "start"
                PropertyAnimation{targets: [btn1, btn2, btn3]; properties: "opacity"; duration:dur}
            }
        ]

        RowLayout{
            Layout.maximumHeight: parent.height/9
            Layout.minimumWidth: parent.width
            Rect{
                id:back
                ctext:"go back"
                Layout.minimumWidth: win.width/3
                Layout.fillHeight: true
                visible: false;
                ccolor:"lightgrey"
                MouseArea{
                    anchors.fill:parent
                    onClicked:{
                        layout.state = "start"
                    }
                }
            }
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
                        layout.state = "item1"
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
                        layout.state = "item2"
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
                        layout.state = "item3"
                    }
                }
            }
        }
    }
}
