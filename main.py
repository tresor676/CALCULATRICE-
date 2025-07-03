from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Charger le fichier .kv (interface)
Builder.load_file("calculator.kv")

class Calculator(BoxLayout):
    def clear_display(self):
        self.ids.display.text = ""

    def backspace(self):
        self.ids.display.text = self.ids.display.text[:-1]

    def add_text(self, value):
        self.ids.display.text += value

    def calculate_result(self):
        try:
            expression = self.ids.display.text
            result = str(eval(expression))
            self.ids.display.text = result
        except:
            self.ids.display.text = "Erreur"

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalculatorApp().run()
