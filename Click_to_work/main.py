from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

class Ui(ScreenManager):
    pass

class MainApp(MDApp):#personalizar temas
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Purple"
        Builder.load_file('main.kv')
        return Ui()

if __name__=='__main__':
    MainApp().run()
