import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.2
Page{
    id:root
    property alias backgroundColor:back_fon.color
    property alias btext:btn.text
    property alias headerText:headerText.text
    signal buttonClicked();
    signal popButton();

    header: ToolBar{
        id:page_header
        height:40
        RowLayout   {
            ToolButton  {
                id:back_btn
                rightPadding: 10
                Text {
                    text: "<-"
                    font.pixelSize: 24
                    visible:stack_view.depth > 1
                    anchors.verticalCenter: parent.verticalCenter
                }
                onClicked: {
                    root.popButton()
                }
            }
            Text{
                id:headerText
                anchors.centerIn: page_header
            }
        }   
    }

    background: Rectangle {
        id:back_fon
    }

    Button {
        id:btn
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.margins: defMargin
        onClicked: {
            root.buttonClicked()
        }
    }
}
