'''
created on Apr 19, 2022

@author Papan Das
'''


from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def on_button_click(self, caption):
        print(f'Controller <<button clicked: {caption}>>')
        result = self.model.calculate(caption)
        print(f'Controller <<Results - {result}>>')
        self.view.value_var.set(result)


