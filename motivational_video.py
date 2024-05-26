# pip install ffpyplayer

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.popup import Popup
import os

class MotivationalApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)


        quotes_button = Button(text='Show Motivational Quotes', size_hint_y=None, height=50)
        quotes_button.bind(on_press=self.show_quotes)
        main_layout.add_widget(quotes_button)


        videos_button = Button(text='Show Motivational Videos', size_hint_y=None, height=50)
        videos_button.bind(on_press=self.show_videos)
        main_layout.add_widget(videos_button)

        return main_layout

    def show_quotes(self, instance):

        quotes = [
            "Мотивація - то є сильно. - МС ПЕТЯ"
        ]


        quotes_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        for quote in quotes:
            quote_label = Label(text=quote, size_hint_y=None)
            quotes_layout.add_widget(quote_label)

        close_button = Button(text='Close', size_hint_y=None, height=50)
        close_button.bind(on_press=lambda x: quotes_popup.dismiss())
        quotes_layout.add_widget(close_button)

        quotes_popup = Popup(title='Motivational Quotes', content=quotes_layout, size_hint=(0.8, 0.8))
        quotes_popup.open()

    def show_videos(self, instance):
        video_urls = [
            'video.mp4', 
        ]


        valid_videos = [url for url in video_urls if os.path.exists(url)]
        if not valid_videos:
            error_popup = Popup(title='Error', content=Label(text='Video file not found!'), size_hint=(0.6, 0.3))
            error_popup.open()
            return

        videos_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        for video_url in valid_videos:
            print(f"Attempting to load video: {video_url}")
            video_player = VideoPlayer(source=video_url, size_hint_y=None, height=300)
            videos_layout.add_widget(video_player)

        close_button = Button(text='Close', size_hint_y=None, height=50)
        close_button.bind(on_press=lambda x: videos_popup.dismiss())
        videos_layout.add_widget(close_button)

        videos_popup = Popup(title='Мотивація', content=videos_layout, size_hint=(0.9, 0.9))
        videos_popup.open()

if __name__ == '__main__':
    MotivationalApp().run()
