import QtQuick 2.15
import QtQuick.Window 2.15

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")
    Rect {
        id: rect1
        width: 10 * 6
        height: 10 * 3
        comColor: "#0c2659"
        y: 50
        z: 9
        anchors.horizontalCenter: parent.horizontalCenter;
       }

    // правая сторона
    Rect {
        id: rect2
        width: 10 *8
        height: 10 * 3
        anchors.bottom: rect1.top;
        anchors.left: rect1.right;
       }
    Rect {
        id: rect5
        width: 10 * 3
        height: 10 * 8
        anchors.top: rect2.bottom;
        anchors.left: rect2.right;
       }
    Rect {
        id: rect14
        width: 10 * 3
        height: 10 * 3
        anchors.top: rect5.bottom;
        anchors.left: rect5.right;
       }
    Rect {
        id: rect15
        width: 10 * 3
        height: 10 * 8
        anchors.top: rect14.bottom;
        anchors.left: rect14.right;
       }
    Rect {
        id: rect16
        width: 10 * 3
        height: 10 * 3
        anchors.top: rect15.bottom;
        anchors.right: rect15.left;
       }
    Rect {
        id: rect17
        width: 10 * 3
        height: 10 * 8
        anchors.top: rect16.bottom;
        anchors.right: rect16.left;
       }
    Rect {
        id: rect18
        width: 10 * 3
        height: 10 * 3
        anchors.top: rect17.bottom;
        anchors.left: rect17.right;
       }
    Rect {
        id: rect19
        width: 10 * 3
        height: 10 * 3
        anchors.top: rect18.bottom;
        anchors.left: rect18.right;
       }
    Rect {
        id: rect20
        width: 10 * 3
        height: 10 * 3
        anchors.top: rect19.bottom;
        anchors.right: rect19.left;
       }
    Rect {
        id: rect21
        width: 10 * 3
        height: 10 * 3
        anchors.top: rect20.bottom;
        anchors.left: rect20.right;
       }

    // левая сторона
    Rect {
        id: rect3
        width: 10 *8
        height: 10 * 3
        anchors.bottom: rect1.top;
        anchors.right: rect1.left;
       }
    Rect {
        id: rect4
        width: 10 * 3
        height: 10 * 8
        anchors.top: rect3.bottom;
        anchors.right: rect3.left;
       }
    Rect {
        id: rect6
        width: 10 * 3
        height: 10 * 3
        anchors.top: rect4.bottom;
        anchors.right: rect4.left;
       }
    Rect {
        id: rect7
        width: 10 * 3
        height: 10 * 8
        anchors.top: rect6.bottom;
        anchors.right: rect6.left;
       }
    Rect {
        id: rect8
        width: 10 * 3
        height: 10 * 3
        anchors.top: rect7.bottom;
        anchors.left: rect7.right;
       }
    Rect {
        id: rect9
        width: 10 * 3
        height: 10 * 8
        anchors.top: rect8.bottom;
        anchors.left: rect8.right;
       }
    Rect {
        id: rect10
        width: 10 * 3
        height: 10 * 3
        anchors.top: rect9.bottom;
        anchors.right: rect9.left;
       }
    Rect {
        id: rect11
        width: 10 * 3
        height: 10 * 3
        anchors.top: rect10.bottom;
        anchors.right: rect10.left;
       }
    Rect {
        id: rect12
        width: 10 * 3
        height: 10 * 3
        anchors.top: rect11.bottom;
        anchors.left: rect11.right;
       }
    Rect {
        id: rect13
        width: 10 * 3
        height: 10 * 3
        anchors.top: rect12.bottom;
        anchors.right: rect12.left;
       }
    Rect {
        id: rect22
        width: 10 * 36
        height: 10 * 3
        anchors.left: rect13.right;
        anchors.top: rect13.top;
       }

    //

    Green {
        id: green1
        width: 10 * 28
        height: 10 * 40
        y: 50
        z: -1
        anchors.horizontalCenter: parent.horizontalCenter;
    }

    Green {
        id: green2
        width: 10 * 3
        height: 10 * 8
        anchors.top: rect6.bottom;
        anchors.left: rect7.right;
       }

    Green {
        id: green3
        width: 10 * 3
        height: 10 * 8
        anchors.top: rect14.bottom;
        anchors.right: rect15.left;
       }

    Green {
        id: green4
        width: 10 * 3
        height: 10 * 3
        anchors.bottom: rect12.top;
        anchors.left: rect13.right;
       }

    Green {
        id: green5
        width: 10 * 3
        height: 10 * 3
        anchors.bottom: rect20.top;
        anchors.right: rect21.left;
       }

    // внутренний контур

    DarkGreen {
        id: dark_green1
        width: 10 * 3
        height: 10 * 3
        anchors.top: rect9.top;
        anchors.left: rect9.right;
       }

    DarkGreen {
        id: dark_green2
        width: 10 * 16
        height: 10 * 3
        anchors.top: dark_green1.bottom;
        anchors.left: dark_green1.right;
       }

    DarkGreen {
        id: dark_green3
        width: 10 * 3
        height: 10 * 3
        anchors.bottom: dark_green2.top;
        anchors.left: dark_green2.right;
       }

    // левая щека

    Cheek {
        id: cheek1
        width: 10 * 3
        height: 10 * 3
        anchors.bottom: dark_green1.top;
        anchors.right: dark_green1.left;
       }

    Cheek {
        id: cheek2
        width: 10 * 3
        height: 10 * 3
        anchors.bottom: cheek1.top;
        anchors.left: cheek1.left;
       }

    // левый глаз

    Eye {
        id: eye1
        width: 10 * 6
        height: 10 * 9
        anchors.bottom: cheek2.top;
        anchors.left: cheek2.right;
       }

    Eye {
        id: eye2
        width: 10 * 3
        height: 10 * 9
        comColor: "black"
        anchors.bottom: cheek2.top;
        anchors.left: cheek2.right;
       }

    // правая щека

    Cheek {
        id: cheek3
        width: 10 * 3
        height: 10 * 3
        anchors.bottom: dark_green3.top;
        anchors.right: dark_green3.right;
       }

    Cheek {
        id: cheek4
        width: 10 * 3
        height: 10 * 3
        anchors.bottom: cheek3.top;
        anchors.left: cheek3.left;
       }

    // левый глаз

    Eye {
        id: eye3
        width: 10 * 6
        height: 10 * 9
        anchors.bottom: cheek4.top;
        anchors.right: cheek4.right;
       }

    Eye {
        id: eye4
        width: 10 * 3
        height: 10 * 9
        comColor: "black"
        anchors.bottom: cheek4.top;
        anchors.left: eye3.left;
       }

    // лапа левая

    DarkGreen {
        id: dark_green4
        width: 10 * 3
        height: 10 * 8
        comColor: "#01bd07";
        anchors.top: dark_green1.bottom;
        anchors.right: dark_green1.right;
       }

    DarkGreen {
        id: dark_green5
        width: 10 * 3
        height: 10 * 3
        anchors.top: dark_green4.bottom;
        anchors.right: dark_green4.right;
       }

    DarkGreen {
        id: dark_green6
        width: 10 * 3
        height: 10 * 3
        anchors.top: dark_green5.bottom;
        anchors.left: dark_green5.right;
       }

    // лапа правая

    DarkGreen {
        id: dark_green7
        width: 10 * 3
        height: 10 * 8
        comColor: "#01bd07";
        anchors.top: dark_green3.bottom;
        anchors.right: dark_green3.right;
       }

    DarkGreen {
        id: dark_green8
        width: 10 * 3
        height: 10 * 3
        anchors.top: dark_green7.bottom;
        anchors.right: dark_green7.right;
       }

    DarkGreen {
        id: dark_green9
        width: 10 * 3
        height: 10 * 3
        anchors.top: dark_green8.bottom;
        anchors.right: dark_green8.left;
       }


}
