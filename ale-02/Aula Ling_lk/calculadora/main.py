from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.config import Config
from kivy.graphics import Color, Ellipse

Config.set('graphics', 'width', '320') 
Config.set('graphics', 'height', '510')
Config.set('graphics', 'resizable', 0)  
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

class MeuApp(BoxLayout):
    def __init__(self, **kwargs):
        super(MeuApp, self).__init__(**kwargs)
        self.ids.meu_botao.text = "Novo Texto"

class BotaoCircular(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (100, 100)
        self.background_color = (0.4, 0.4, 0.4, 1)
        self.background_normal = ''
        self.background_down = ''
        self.canvas.before.add(Color(0.2, 0.2, 0.2, 1))
        self.canvas.before.add(Ellipse(pos=self.pos, size=self.size))

    def on_size(self, *args):
        self.canvas.before.clear()
        self.canvas.before.add(Color(0.2, 0.2, 0.2, 1))
        self.canvas.before.add(Ellipse(pos=self.pos, size=self.size))

class BotaoCustomizado(Button):
    pass

class MeuBotao(Button):
    pass

class AplicativoCalculadora(App):
    def build(self):
        return Calculadora()

if __name__ == '__main__':
    AplicativoCalculadora().run()
