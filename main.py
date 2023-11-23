from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.camera import Camera


from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage

from deepface import DeepFace
from kivymd.uix.label import MDLabel
import os
import glob
from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '800')



class CameraExample(MDApp, App):
    def build(self):
        self.count_img = 0
        self.layout = FloatLayout()

        self.text = MDLabel(text="подобрать фильм по настроению", size_hint=(.6, .1), pos_hint={'x': .3, 'y': .85})

        self.cameraObject = Camera(play=False)
        self.cameraObject.play = True
        self.cameraObject.resolution = (400, 300)  # Specify the resolution


        self.take_photo = Button(text='Сделать\n  Фото', size_hint=(.3, .07), pos_hint={'x': .35, 'y': .1})
        self.take_photo.bind(on_press=self.onCameraClick)

        self.layout.add_widget(self.text)
        self.layout.add_widget(self.cameraObject)
        self.layout.add_widget(self.take_photo)

        return self.layout

    def onCameraClick(self, *args):
        self.cameraObject.export_to_png('img/selfie'+str(self.count_img)+'.png')
        self.emotion()
        setattr(self.cameraObject, 'opacity', 0)


        self.done = Button(text='Готово', size_hint=(.2, .07), pos_hint={'x': .1, 'y': .1})
        self.done.bind(on_press=self.okeyy)
        self.layout.add_widget(self.done)


        self.take_photo_omt = Button(text='Сделать фото\n   ещё раз', size_hint=(.3, .07), pos_hint={'x': .65, 'y': .1})
        self.take_photo_omt.bind(on_press=self.change)

        self.layout.add_widget(self.take_photo_omt)
        self.img = Image(source='img/selfie'+str(self.count_img)+'.png')
        self.layout.add_widget(self.img)
        self.layout.remove_widget(self.take_photo)

        return self.layout

    def emotion(self):
        try:
            result_dict = DeepFace.analyze(img_path='img/selfie'+str(self.count_img)+'.png', actions=['emotion'])
            self.layout.remove_widget(self.text)
            self.text = MDLabel(text=result_dict[0].get('dominant_emotion'), size_hint=(.6, .1), pos_hint={'x': .3, 'y': .85})
            print(result_dict[0].get('dominant_emotion'))
            self.layout.add_widget(self.text)
            return self.layout

        except Exception as _ex:
            return _ex
    def change(self, *args):
        self.count_img += 1
        setattr(self.cameraObject, 'opacity', 1)
        self.layout.remove_widget(self.img)
        self.layout.remove_widget(self.done)
        self.layout.remove_widget(self.take_photo_omt)
        self.take_photo = Button(text='Сделать\n  Фото', size_hint=(.3, .07), pos_hint={'x': .35, 'y': .1})
        self.take_photo.bind(on_press=self.onCameraClick)

        self.layout.add_widget(self.take_photo)

    def okeyy(self, *args):
        files = glob.glob('img/*')
        for f in files:
            os.remove(f)


# Start the Camera App

if __name__ == '__main__':
    CameraExample().run()

