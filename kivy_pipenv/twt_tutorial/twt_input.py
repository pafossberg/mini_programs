from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle, Color, Line

class Touch(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(0, 1, 0, 0.5, mode='rgba')
            Line(points=(20, 30, 400, 500, 60, 900), width=(50))
            Color(1, 0, 0, 0.5, mode='rgba')
            self.rect = Rectangle(pos=(0,0), size=(50,50))

    # Heila skjermen blir clickable uten denne super funksjonen
    # Men med denna super funksjonen i kver method så funke kanppen  
    # super().on_touch_down(touch) 
    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Down", touch)   

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Move", touch)

class UserInput(App):
    def build(self):
        return Touch()


if __name__ == '__main__':
    UserInput().run()
