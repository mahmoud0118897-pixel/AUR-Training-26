import QtQuick
import QtQuick.Shapes

Rectangle {
    id: root
    anchors.fill: parent
    color: "#1e1e1e" // Dark background matching design
    
    property var clockData: dataBridge

    readonly property int hours: clockData ? clockData.hours : 0
    readonly property int minutes: clockData ? clockData.mins : 0
    readonly property int seconds: clockData ? clockData.secs : 0

    // Outer Dial Edge
    Rectangle {
        id: dial 
        anchors.centerIn: root
        width: (parent.width > parent.height ) ? parent.height : parent.width * 0.85
        height: width
        radius: width / 2
        color: "#ffffff"
        border.color: "#3a3a3a"
        border.width: 12


        Repeater {
            model: 60
            Rectangle {
                required property int index
                readonly property bool isMajor: index % 5 === 0
                width: isMajor ? 3 : 1.5
                height: isMajor ? 12 : 6
                color: "#000000"
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.top: parent.top
                anchors.topMargin: 8
                transformOrigin: Item.Bottom
                transform: Rotation {
                    origin.x: width / 2
                    origin.y: dial.height / 2 - 8
                    angle: index * 6
                }
            }
        }

        // Hour Numbers (1 to 12)
        Repeater {
            model: 12
            Text {
                required property int index
                readonly property real angle: (index + 1) * 30 * Math.PI / 180
                readonly property real radius: dial.width / 2 - 32
                text: (index + 1).toString()
                font.pixelSize: 18
                font.bold: true
                color: "#000000"
                x: dial.width / 2 + radius * Math.sin(angle) - width / 2
                y: dial.height / 2 - radius * Math.cos(angle) - height / 2
            }
        }

        // Hour Hand
        Shape {
            id:pointer
            anchors.topMargin: parent.height*0.18
            anchors.top: parent.top
            anchors.bottom: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width * 0.05
            rotation: (root.hours + root.minutes / 60) * 30
            transformOrigin: Item.Bottom

            ShapePath {
                strokeWidth: 1
                strokeColor: "black"
                fillColor: "black"
                startX: 0
                startY: pointer.height 
                PathLine { x: pointer.width /2; y: 0 }
                PathLine { x: pointer.width ; y: pointer.height }
                PathLine { x: 0 ; y: pointer.height }
            }
        }

        //Minute Hand
        Shape {
            id:pointer_min
            anchors.topMargin: parent.height*0.1
            anchors.top: parent.top
            anchors.bottom: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width * 0.04
            rotation: (root.minutes + root.seconds / 60) * 6
            transformOrigin: Item.Bottom

            ShapePath {
                strokeWidth: 1
                strokeColor: "black"
                fillColor: "black"
                startX: 0
                startY: pointer.height
                PathLine { x: pointer_min.width /2; y: 0 }
                PathLine { x: pointer_min.width ; y: pointer_min.height }
                PathLine { x: 0 ; y: pointer_min.height }
            }
        }

        // Second Hand
        Rectangle {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottom: parent.verticalCenter
            width: 2
            height: dial.height * 0.42
            color: "#e60000"
            transformOrigin: Item.Bottom
            rotation: root.seconds * 6
        }

        
        Rectangle {
            anchors.centerIn: parent
            width: 12
            height: 12
            radius: 6
            color: "#000000"
        }
    }
}