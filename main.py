from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.uix.list import OneLineAvatarListItem, ImageLeftWidget
import time
class Homescreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mycamera = self.ids.camera
        self.myimage = Image()
        self.resultbox = self.ids.resultbox
        self.mybox = self.ids.mybox

    def captureyouface(self):

        timenow = time.strftime("%Y%m%d_%H%M%S")
        self.mycamera.export_to_png("image_{}.png".format(timenow))
        self.myimage.source = "image_{}.png".format(timenow)
        self.resultbox.add_widget(
            OneLineAvatarListItem(
                ImageLeftWidget(
                    source="image_{}.png".format(timenow),
                    size_hint_x=0.3,
                    size_hint_y=1,
                    size=(300, 300)

                ),
                text=self.ids.name.text
            )
        )
class MyApp(MDApp):
    def build(self):
        Window.size = (360, 800)
        return Homescreen()

Builder.load_string("""
<Homescreen>:
    name: 'camerascreen'
    MDScrollView:
        do_scroll_x:False
        do_scroll_y:True
        MDBoxLayout:
            id:mybox
            orientation: 'vertical'
            size_hint_y: 0.9
            pos_hint:{"center_y":0.8}
            padding:10
            spacing:10
            Camera:
                id:camera
                resolution:(800,800)
                play:True
            MDTextField:
                id:name
                hint_text:"youname"
                font_size: 30
            MDRaisedButton:
                text:"capture"
                on_release:root.captureyouface()
            MDList:
                id:resultbox
""")

if __name__ == "__main__":
    MyApp().run()