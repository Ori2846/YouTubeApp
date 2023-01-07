from flask import Flask, request, render_template
from flask import send_from_directory
from pytube import YouTube
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download', methods=['POST'])
def download():
    # get the YouTube URL from the form submission
    url = request.form['url']

    # create a YouTube object using the URL
    yt = YouTube(url)

    # get the first video in the list of available videos
    video = yt.streams.filter(res='1080p', file_extension='mp4').first()

    # save the video to a local file
    video.download('./videos')
    # get the file name of the downloaded video
    file_name = video.default_filename

    # send the video file as a response to the request
    return send_from_directory('./videos', file_name, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)