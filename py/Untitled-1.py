from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

KV = '''


Box:
    img:img
    FloatLayout:
        padding: "5dp"
        spacing: "5dp"
        size_hint: 1,1

        Image:
            id: img
            source: "static\\img\\Lexapro.png"
            size_hint: 0.45,0.45
            keep_ratio: True
            pos_hint: {'center_x': 0.5,'center_y': 0.75}
            on_touch_down: root.on()
        BoxLayout:
            orientation: "vertical"
            size_hint_y: None
            size_hint_x: 0.45
            height: self.minimum_height
            spacing: "5dp"
            pos_hint: {'center_x': 0.5,'center_y': 0.25}
            MDTextField:
                hint_text: "Dose"
                size_hint_y: None
                height: "5dp"
                font_size: 10

            MDTextField:
                hint_text: "Tempo"
                size_hint_y: None
                height: "5dp"
                font_size:10

            MDTextField:
                hint_text: "Tempo"
                size_hint_y: None
                height: "5dp"
                font_size:10

            MDRoundFlatButton:
                text: "Adicionar"
                size_hint_y: None
                height: "5dp"
                font_size:10

            MDRoundFlatButton:
                text: "Erase"
                size_hint_y: None
                height: "5dp"
                font_size:10
'''
class Box(MDBoxLayout):
    ''' Box class for the popup'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.img = ObjectProperty(None)
        self.pop = Popup(title='Test popup', size_hint=(0.8,0.8), disabled=True)

    def on(self):
        if self.img.on_touch_down:

            self.pop.content = Image(source= self.img.source)
            self.pop.open()


class MainApp(MDApp):
    def build(self):

        return Builder.load_string(KV)


if __name__ == "__main__":
    MainApp().run()
