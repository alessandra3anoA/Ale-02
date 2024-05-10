from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
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

class AplicativoCalculadora(App):
    def build(self):
        return Calculadora()

if __name__ == '__main__':
    AplicativoCalculadora().run()