import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    width: 400
    height: 300
    visible: true
    title: "Hello World QML"

    Text {
        anchors.centerIn: parent
        text: "Hello World"
        font.pixelSize: 24
    }
}