import QtQuick
import QtQuick.Window
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Windows

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Simple PPT")

    GridLayout{
        anchors.centerIn: parent
        Layout.row: 0
        Layout.column: 0
        Button{
            text: qsTr("Make PPT")
            Layout.rowSpan: 2
            Layout.columnSpan: 2
        }
    }
}
