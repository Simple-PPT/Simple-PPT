import QtQuick
import QtQuick.Window
import QtQuick.Layouts
import QtQuick.Controls

Window {
    visible: true
    width: 640
    height: 480
    title: "Simple PPT"
    StackView{
    
    }
    Component{
        GridLayout{
            rows: 12
            columns: 12
            Button{
                Layout.row: 0
                Layout.column: 0
                text: qsTr("Make PPT")
                Layout.rowSpan: 2
                Layout.columnSpan: 1

                onClicked: {
                    console.log("Hello hello")
                }
            }
        }
    }
}
