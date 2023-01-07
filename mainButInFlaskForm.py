from flask import Flask, request, render_template
from flask import send_from_directory
from pytube import YouTube
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    yt = YouTube(url)
    video = yt.streams.filter(res='1080p', file_extension='mp4').first()
    video.download('./videos')
    file_name = video.default_filename
    return send_from_directory('./videos', file_name, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)