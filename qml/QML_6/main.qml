import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.2
Window {
    width: 360
    height: 640
    visible: true
    title: qsTr("StackView_test")
    property int defMargin:10

    StackView {
        id:stack_view
        anchors.fill: parent
        initialItem: page1
    }

    My_Page {
        id: page1
        btext: "To_Green"
        headerText: "Red"
        backgroundColor: "red"
        onButtonClicked: {
          stack_view.push(page2)
        }
        onPopButton: {
            stack_view.pop()
        }
    }

    My_Page {
        id: page2
        visible: false
        btext: "To_Yellow"
        headerText: "Green"
        backgroundColor: "green"
        onButtonClicked: {
          stack_view.push(page3)
        }
        onPopButton: {
            stack_view.pop()
        }
    }

    My_Page {
        id: page3
        visible: false
        btext: "To_Red"
        headerText: "Yellow"
        backgroundColor: "yellow"
        onButtonClicked: {
          stack_view.push(page1)
        }
        onPopButton: {
            stack_view.pop()
        }
    }
}
