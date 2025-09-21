from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

VIDEO_DIR = os.path.join(os.path.dirname(__file__), 'videos')

@app.route('/')
def index():
    videos = os.listdir(VIDEO_DIR)
    return render_template('index.html', videos=videos)

@app.route('/videos/<filename>')
def videos(filename):
    return send_from_directory(VIDEO_DIR, filename)

@app.route('/users/<username>')
def user_profile(username):
    # Псевдо-профиль
    return render_template('user_profile.html', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

