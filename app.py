from flask import Flask, render_template, Response
import cv2
from object_detection import detect_objects
from drone_controller import DroneSimulator

app = Flask(__name__)
drone = DroneSimulator()
camera = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            frame = detect_objects(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/takeoff')
def takeoff():
    return drone.takeoff(10)

@app.route('/land')
def land():
    return drone.land()

if __name__ == "__main__":
    app.run(debug=True)