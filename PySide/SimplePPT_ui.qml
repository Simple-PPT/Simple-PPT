import QtQuick
import QtQuick.Controls.Windows as Windows
import QtQuick.Layouts
import QtQuick.Window

Window{
    title: qsTr("Simple PPT")
    Rectangle {
        width: 300
        height: 300
        GridLayout{
            anchors.centerIn: parent
        }
    }
}
