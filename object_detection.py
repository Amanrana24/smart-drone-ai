from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect_objects(frame):
    results = model(frame)
    annotated_frame = results[0].plot()
    return annotated_frame