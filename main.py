from camera import Video
import flask as fsk


app = fsk.Flask(__name__)

@app.route('/')

def index():
    return fsk.render_template('index.html')

position = "NULL"
area = "NULL"
def gen(camera):
    while True:
        global position
        global area
        global ball
        frame, position, area, ball = camera.main_exec()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
@app.route('/video_feed')
def video_feed():
    return fsk.Response(gen(Video()),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/status')
def status():
    present = "FALSE"
    global area
    if area != '0.0' and area!="NULL":
        if " %" not in area:
            area+=" %"
    else:
        area = "NULL"
    if (position!="NULL"):
        present = "TRUE"
    else:
        present = "FALSE"
    print(present, position, area)
    return fsk.jsonify(present = present, position = position, area = area)

@app.route('/font')
def font():
    filename = 'static/Azonix.otf'
    return fsk.send_file(filename, mimetype='font/otf')

@app.route('/github')
def github():
    return fsk.redirect("https://github.com/hariketsheth/TCR_Task_1")

app.run(debug=True)
