from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen 

class Tempate_Button(Button): 
    def __init__(self, screen, direction="right", goal="main", **kwargs):
        super().__init__(**kwargs) # запускаємо конструкто класу Button
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self): # при натисканні (напрямок, екран для зміни)
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class Start_Window(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        button = Tempate_Button(self, direction="left",goal="main",text="відкрити")
        label = Label(text="Оберіть дію")
        layout = BoxLayout()
        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)

class Main_Window(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

class MyApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(Start_Window(name="start"))
        manager.add_widget(Main_Window(name="main"))
        return manager

if __name__ == '__main__':
    app = MyApp()
    app.run()
