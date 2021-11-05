import QtQuick 2.12
import QtQuick.Controls 2.12

Rectangle {
    id:main
    width: 400
    height: 200
    gradient: gradientColorRed

    property bool run_server: false

    Gradient{
        id :gradientColorGreen
        GradientStop { position: 0.0; color: "#003728" }
        GradientStop { position: 0.6; color: "#00f68e" }
        GradientStop { position: 1; color: "#003728" }
    }

    Gradient{
        id :gradientColorRed
        GradientStop { position: 0.0; color: "#5e0404" }
        GradientStop { position: 0.6; color: "#ed1f1f" }
        GradientStop { position: 1; color: "#5e0404" }
    }

    FontLoader{id:byekan ;source: "font/byekan.ttf"}

    Label {
        x: 46
        y: 43
        width: 311
        height: 52
        color: "#FDFDFD"
        font.pixelSize: 25
        font.family: byekan.name
        text: qsTr("راه انداز سرور")
        horizontalAlignment: Text.AlignHCenter
    }

    Column{
        x: 19
        y: 125
        spacing: 10

        Button {
            width: 364
            height: 39
            text: "اجرای سرور"
            font.family: byekan.name
            font.pixelSize: 18
            onClicked:{
                run_server = qmlToQt.runServer(run_server)

                if(!run_server){
                    text = "اجرای سرور"
                    main.gradient = gradientColorRed
                }
                else{
                    text = "بستن سرور"
                    main.gradient = gradientColorGreen
                }
            }
        }
    }


}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.1}
}
##^##*/
