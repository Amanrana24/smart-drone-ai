# 🚁 SmartDrone-AI

An AI-powered autonomous drone simulation system with real-time object detection and web dashboard control.

## Features

- Real-time YOLOv8 object detection
- Live video stream
- Drone takeoff & landing control
- GPS simulation
- Web dashboard

## Tech Stack

Python, Flask, OpenCV, YOLOv8, DroneKit

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```
![Drone Detection Demo](static/demo.png)
<img width="497" height="362" alt="smart-drone-ai:static:demo" src="https://github.com/user-attachments/assets/742859ec-7bf1-4bd3-91ad-e3d3944a3548" />


⚠️ Notes

Model weights (yolov8n.pt) are downloaded automatically on first run.

Model files are excluded from GitHub for repository optimization.

Designed for local simulation (webcam required).

📊 Future Improvements

Autonomous navigation path planning

Multi-object tracking (DeepSORT)

Alert notification system

Map-based drone monitoring

Cloud deployment version

Edge AI deployment

👨‍💻 Author

Aman Deep
Computer Science & AI Enthusiast

📜 License

MIT License
