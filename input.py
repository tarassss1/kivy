from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import os

class NoteTakingApp(App):
    def build(self):
        self.notes_file = 'notes.txt'
        self.load_notes()

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.text_input = TextInput(hint_text='Enter your note here', size_hint_y=None, height=100)
        main_layout.add_widget(self.text_input)

        save_button = Button(text='Save Note', size_hint_y=None, height=50)
        save_button.bind(on_press=self.save_note)
        main_layout.add_widget(save_button)

        self.scroll_view = ScrollView(size_hint=(1, None), height=300)
        self.notes_label = Label(text=self.notes, size_hint_y=None, markup=True)
        self.notes_label.bind(texture_size=self._update_label_height)
        self.scroll_view.add_widget(self.notes_label)
        main_layout.add_widget(self.scroll_view)

        return main_layout

    def _update_label_height(self, instance, value):
        instance.height = instance.texture_size[1]

    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, 'r') as file:
                self.notes = file.read()
        else:
            self.notes = ""

    def save_note(self, instance):
        new_note = self.text_input.text
        if new_note:
            self.notes += new_note + "\n"
            self.notes_label.text = self.notes
            self.text_input.text = ""
            with open(self.notes_file, 'w') as file:
                file.write(self.notes)

if __name__ == '__main__':
    NoteTakingApp().run()
