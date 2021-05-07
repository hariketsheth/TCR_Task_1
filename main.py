from camera import Video
from flask import Flask, render_template, Response,jsonify,send_file, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.main_exec()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
@app.route('/video_feed')
def video_feed():
    return Response(gen(Video()),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/font')
def font():
    filename = 'static/Azonix.otf'
    return send_file(filename, mimetype='font/otf')

@app.route('/github')
def github():
    return redirect("https://github.com/hariketsheth/TCR_Task_1")
app.run()
