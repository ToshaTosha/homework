import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls
import QtQuick.Layouts 1.12

Window {
    width: 480
    height: 600
    title: 'Login_Page'
    visible: true

    property string passwordField: ""

    ColumnLayout {
        spacing: 20
        anchors.centerIn: parent
        
        Text {
            text: "Enter your password:"
            font.pixelSize: 16
            Layout.alignment: Qt.AlignCenter
        }

        Rectangle {
            color: "transparent"
            Layout.preferredWidth: parent
            Layout.preferredHeight: 50
            Layout.alignment: Qt.AlignCenter

            Row {
                spacing: 6
                anchors.centerIn: parent
                Repeater {
                    model: 6
                    Label {
                        width: 20
                        height: 20
                        font.pixelSize: 36
                        text: "*"
                        Layout.alignment: Qt.AlignCenter
                        color: index < passwordField.length ? "black" : "lightgrey"
                    }
                }
            }
        }

        GridLayout {
            width: parent.width
            columns: 3
            rows: 4

            Repeater {
                model: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "", "0", "C"]
                Button {
                    text: modelData
                    onClicked: {
                        if (text === "C") {
                            passwordField = "";
                        } else {
                            passwordField += text;
                        }
                    }
                    Layout.fillWidth: true
                    Layout.preferredHeight: 50
                }
            }
        }
    }
}
