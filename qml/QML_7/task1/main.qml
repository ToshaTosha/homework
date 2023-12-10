import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls
import QtQuick.Layouts 1.12

Window {
    width: 480
    height: 600
    title: 'Login_Page'
    visible: true

    ColumnLayout {
        spacing: 20
        anchors.centerIn: parent

        TextField {
            id: username
            placeholderText: "Username"
            font.pixelSize: 16
            background: Rectangle {
                implicitWidth: 200
                implicitHeight: 35
                border.color: 'grey'
            }
        }

        TextField {
            id: pass
            placeholderText: "Password"
            font.pixelSize: 16
            echoMode: TextInput.Password
            background: Rectangle {
                implicitWidth: 200
                implicitHeight: 35
                border.color: 'grey'
            }
        }

        RowLayout{
            spacing: 10
            Button {
                text: "Log In"
                font.pixelSize: 14
            }
            Button {
                text: "Clear"
                font.pixelSize: 14
                onClicked: {
                    pass.text = ""
                    username.text = ""
                }
            }
        }
    }
}
