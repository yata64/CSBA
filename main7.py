from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class Quadro(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (400, 300)
        self.limpar()

    def limpar(self):
        self.ids.mensagem.text = " "
        self.ids.op1.text = " "
        self.ids.op2.text = " "
        self.ids.resultado.text = " "

    def desligar(self):
        App.get_running_app().stop()

    def distancia_entre_n(self):
        try: 
            o1 = float(self.ids.op1.text)
            o2 = float(self.ids.op2.text)

            if o1 > o2:
                self.ids.resultado.text = str(o1-o2)

            else:
                self.ids.resultado.text = str(o2-o1)

        except: 
            self.ids.mensagem.text = \
            "[color=#FF0000] Favor fornecer os operandos corretamente!![/color]"

    def n_maior(self):
        try: 
            o1 = float(self.ids.op1.text)
            o2 = float(self.ids.op2.text)
            if o1 > o2:
                self.ids.resultado.text = str(o1) 
            
            else: 
                self.ids.resultado.text = str(o2)

        except: 
            self.ids.mensagem.text = \
            "[color=#FF0000] Favor fornecer os operandos corretamente!![/color]"

    def n_menor(self):
        try: 
            o1 = float(self.ids.op1.text)
            o2 = float(self.ids.op2.text)
            if o1 > o2:
                self.ids.resultado.text = str(o2) 
            
            else: 
                self.ids.resultado.text = str(o1)

        except: 
            self.ids.mensagem.text = \
            "[color=#FF0000] Favor fornecer os operandos corretamente!![/color]"
    
    def par_impar(self):
        try:
            o1 = float(self.ids.op1.text)
            o2 = float(self.ids.op2.text)
            msg = " "
            
            if o1 % 2 == 0: 
                msg += f"[color=#FF0000]{o1} é par!![/color]\n"

            else: 
                msg += f"[color=#FF0000]{o1} é par!![/color]\n"
            
            if o2 % 2 == 0: 
                msg += f"[color=#FF0000]{o2} é par!![/color]"

            else: 
                msg += f"[color=#FF0000]{o2} é par!![/color]"
        except:
            self.ids.mensagem.text = \
            "[color=#FF0000] Favor fornecer os operandos corretamente!![/color]"

class interfaceApp(App):

    def build(self):
        self.title = "Calculadora"
        return Quadro()

meuApp = interfaceApp()