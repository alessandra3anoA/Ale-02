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

    def limpar_um_caracter(self):
        self.ids.display.text = self.ids.display.text[:-1]
        
    def inverter_sinal(self):
        texto_atual = self.ids.display.text
        if texto_atual and texto_atual[0] != '-':
            self.ids.display.text = '-' + texto_atual
        elif texto_atual:
            self.ids.display.text = texto_atual[1:]

    def on_textinput(self, text):
        self.atualizar_display(text)

class AplicativoCalculadora(App):
    def build(self):
        return Calculadora()

if __name__ == '__main__':
    AplicativoCalculadora().run()
