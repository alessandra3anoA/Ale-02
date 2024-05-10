from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculadoraApp(App):

    def build(self):
        self.expressao = ""
        layout = GridLayout(cols=4, spacing=10)

        self.entrada_texto = TextInput(multiline=False, readonly=True, font_size=40)
        layout.add_widget(self.entrada_texto)

        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for botao in botoes:
            if botao == '=':
                botao_igual = Button(text=botao, background_color=(0.1, 0.6, 0.3, 1))
                botao_igual.bind(on_press=self.calcular)
                layout.add_widget(botao_igual)
            elif botao == 'C':
                botao_limpar = Button(text=botao, background_color=(0.8, 0.1, 0.1, 1))
                botao_limpar.bind(on_press=self.limpar)
                layout.add_widget(botao_limpar)
            else:
                btn = Button(text=botao)
                btn.bind(on_press=self.on_press_botao)
                layout.add_widget(btn)

        return layout

    def on_press_botao(self, instance):
        self.expressao += instance.text
        self.entrada_texto.text = self.expressao

    def limpar(self, instance):
        self.expressao = ""
        self.entrada_texto.text = self.expressao

    def calcular(self, instance):
        try:
            self.entrada_texto.text = str(eval(self.expressao))
        except Exception:
            self.entrada_texto.text = "Erro"


if __name__ == '__main__':
    CalculadoraApp().run()


