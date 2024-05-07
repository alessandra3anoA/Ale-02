from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.uix.checkbox import CheckBox
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

class BorderedCheckBox(CheckBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update_rectangle, size=self.update_rectangle)

    def update_rectangle(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0, 0)  # Cor preta
            x = self.pos[0]  + self.width * 0.45 
            y = self.pos[1] + self.height * 0.3
            width = self.width * 0.1
            height = self.height * 0.4
            Rectangle(pos=(x, y), size=(width, height), width=2)  # Borda preta

class Telalogin(BoxLayout):
    def __init__(self, **kwargs):
        super(Telalogin, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20

        self.add_widget(AsyncImage(source='https://github.com/MateusN17/Reposit-rio-/blob/main/Kivy/images.png?raw=true'))
        
        self.add_widget(Label(text="Insira o seu E-mail:", color=(0, 0, 0.2, 1),bold=True,font_size= 20))
        self.Email = TextInput(hint_text="Digite seu e-mail aqui.", multiline=False)
        self.add_widget(self.Email)
        
        self.add_widget(Label(text="Insira sua Senha:", color=(0, 0, 0.2, 1),bold=True,font_size= 20))
        self.Senha = TextInput(hint_text="Digite sua senha aqui", multiline=False ,password=True)
        self.add_widget(self.Senha) 
        
        botao_layout = BoxLayout(padding=8)
        self.add_widget(botao_layout)
        
        self.checkbox_layout = BoxLayout(orientation="horizontal", size_hint_y=None,height=40)
        self.add_widget(self.checkbox_layout)

        self.checkbox = BorderedCheckBox()
        self.checkbox_layout.add_widget(self.checkbox)

        self.checkbox_text = Label(text="Aceitar termos e condições", color=(0, 0, 0.2, 1),bold=True,font_size=14)
        self.checkbox_layout.add_widget(self.checkbox_text)
        
        botao_layout = BoxLayout(padding=8)
        self.add_widget(botao_layout)
        
        self.enviar = Button(text="Enviar", background_color=get_color_from_hex('#3498db'))
        self.enviar.bind(on_press=self.Login)
        botao_layout.add_widget(self.enviar)
        
        self.cancelar = Button(text="Cancelar", background_color=get_color_from_hex('#ff0000'))
        self.cancelar.bind(on_press=self.botao_cancelar)
        botao_layout.add_widget(self.cancelar)

        self.esqueceu_senha = Button(text="Esqueceu a Senha?", background_color=get_color_from_hex('#ff8000'), font_size=11)
        self.esqueceu_senha.bind(on_press=self.esqueceu_senha_pressionado)
        botao_layout.add_widget(self.esqueceu_senha)

        self.Email.bind(on_text_validate=self.switch_focus)
        self.Senha.bind(on_text_validate=self.switch_focus)
    
    def switch_focus(self, instance):
        # Função para alternar o foco entre os text inputs ao pressionar Enter
        if instance == self.Email:
            self.Senha.focus = True

    #self.checkbox.active= True

    def Login(self, instance, **kwargs):
        if self.Email.text.strip() == '' or self.Senha.text.strip() == '':
            print("Por favor, preencha todos os campos.")
            self.open_popup2()
        elif not self.checkbox.active:
            print("Você precisa aceitar os termos e condições.")
            self.open_popup1()
        else:
            print("Termos e condições aceitos.")
            print("Nome de usuário:", self.Email.text)
            print("Senha:", self.Senha.text)

    def botao_cancelar(self, instance):
        print("Login cancelado.")
        self.Email.text = ''
        self.Senha.text = ''
        self.checkbox.active = False
        
    def esqueceu_senha_pressionado(self, instance):
        if self.Email.text.strip() == '' or self.Senha.text.strip() == '':
            print("Por favor, preencha todos os campos.")
            self.open_popup2()
        email = self.Email.text
        print(f"O usuário {email} esqueceu a senha?")

    def open_popup1(self):
        box = BoxLayout(orientation="vertical", padding=10, spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)
        ok = Button(text="Ok", on_release=self.close_popup)
        botoes.add_widget(ok)
        box.add_widget(botoes)
        self.popup = Popup(title="Você precisa aceitar os termos e condições.", content=box, size_hint=(None,None), size=(200,150))
        self.popup.open()
    def confirmacao_telalogin(self, *args):
        Telalogin().open_popup1()

    def open_popup2(self):
        box = BoxLayout(orientation="vertical", padding=10, spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)
        ok = Button(text="Ok", on_release=self.close_popup)
        botoes.add_widget(ok)
        box.add_widget(botoes)
        self.popup = Popup(title="Por favor, preencha todos os campos.", content=box, size_hint=(None,None), size=(200,150))
        self.popup.open()
    def confirmacao_telalogin(self, *args):
        Telalogin().open_popup2()
    def close_popup(self, *args):
        self.popup.dismiss()


class Umatela(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return Telalogin()

if __name__ == '__main__':
    Umatela().run()

Window.size = (360, 640)  

if __name__ == '__main__':
    Umatela().run()
