from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.config import Config
from kivy.graphics import Color, RoundedRectangle
Config.set('graphics', 'width', '370') 
Config.set('graphics', 'height', '640')
Builder.load_file('main.kv')

class Calculadora(BoxLayout):
    def atualizar_display(self, texto):
        self.ids.display.text += texto

    def limpar_display(self):
        self.ids.display.text = ''

    def calcular(self):
        try:
            self.ids.display.text = str(eval(self.ids.display.text))
        except Exception as e:
            self.ids.display.text = 'Erro'
class BotaoRedondo(Button):
    def __init__(self, **kwargs):
        super(BotaoRedondo, self).__init__(**kwargs)
        self.background_color = (0.2, 0.2, 0.2, 1)
        self.font_size = 20
        self.size_hint = (None, None)
        self.size = (100, 100)
        self.canvas.before.add(Color(rgba=self.background_color))
        self.canvas.before.add(RoundedRectangle(size=self.size, pos=self.pos, radius=[20,]))

Builder.load_string

class AplicativoCalculadora(App):
    def build(self):
        return Calculadora()

if __name__ == '__main__':
    AplicativoCalculadora().run()