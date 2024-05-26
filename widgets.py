from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.spinner import Spinner
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel

class MyApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Button
        button = Button(text='Click Me!')


        # TextInput
        textinput = TextInput(hint_text='Enter some text')

        # CheckBox
        checkbox_layout = BoxLayout(orientation='horizontal')
        checkbox_label = Label(text='Do you agree?')
        checkbox = CheckBox()
        checkbox_layout.add_widget(checkbox_label)
        checkbox_layout.add_widget(checkbox)

        # Slider
        slider = Slider(min=0, max=100, value=25)

        # Switch
        switch_layout = BoxLayout(orientation='horizontal')
        switch_label = Label(text='Enable Feature')
        switch = Switch()
        switch_layout.add_widget(switch_label)
        switch_layout.add_widget(switch)

        # Spinner
        spinner = Spinner(
            text='Choose an option',
            values=('Option 1', 'Option 2', 'Option 3', 'Option 4')
        )

        # ProgressBar
        progressbar = ProgressBar(max=1000, value=500)



        # FileChooser
        filechooser = FileChooserListView(size_hint_y=None, height=200)

        # Popup
        def show_popup(instance):
            popup_layout = BoxLayout(orientation='vertical')
            popup_label = Label(text='This is a popup!')
            close_button = Button(text='Close')
            popup_layout.add_widget(popup_label)
            popup_layout.add_widget(close_button)
            popup = Popup(title='Popup Example', content=popup_layout, size_hint=(0.5, 0.5))
            close_button.bind(on_press=popup.dismiss)
            popup.open()

        popup_button = Button(text='Open Popup')
        popup_button.bind(on_press=show_popup)

        # ScrollView
        scrollview = ScrollView(size_hint=(1, None), height=200)
        scroll_label = Label(text='Hello, Kivy!\n' * 20, size_hint_y=None)
        scroll_label.height = scroll_label.texture_size[1]
        scrollview.add_widget(scroll_label)

        # GridLayout
        gridlayout = GridLayout(cols=2, size_hint_y=None)
        gridlayout.bind(minimum_height=gridlayout.setter('height'))
        gridlayout.add_widget(Label(text='Label 1'))
        gridlayout.add_widget(Button(text='Button 1'))
        gridlayout.add_widget(Label(text='Label 2'))
        gridlayout.add_widget(Button(text='Button 2'))
        scroll_grid = ScrollView(size_hint=(1, None), height=200)
        scroll_grid.add_widget(gridlayout)


        main_layout.add_widget(button)
        main_layout.add_widget(textinput)
        main_layout.add_widget(checkbox_layout)
        main_layout.add_widget(slider)
        main_layout.add_widget(switch_layout)
        main_layout.add_widget(spinner)
        main_layout.add_widget(progressbar)

        main_layout.add_widget(filechooser)
        main_layout.add_widget(popup_button)
        main_layout.add_widget(scrollview)
        main_layout.add_widget(scroll_grid)


        return main_layout

if __name__ == '__main__':
    MyApp().run()
