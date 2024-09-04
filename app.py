from flask import Flask, render_template, request, redirect, url_for
import speech_recognition as sr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    text = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file'] 
        if file.filename == '':
            return redirect(request.url)
        if file:
            recognizer = sr.Recognizer()
            with sr.AudioFile(file) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)
    return render_template('index.html', text=text)


if __name__ == '__main__':
    app.run(debug=True)
