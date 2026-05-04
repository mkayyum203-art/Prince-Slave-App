from kivy.app import App
from kivy.uix.label import Label
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return "Server is Running!"

def start_flask():
    app.run(host='0.0.0.0', port=8080)

class MyApp(App):
    def build(self):
        flask_thread = Thread(target=start_flask)
        flask_thread.daemon = True
        flask_thread.start()
        return Label(text='App Running Successfully!')

if __name__ == '__main__':
    MyApp().run()
