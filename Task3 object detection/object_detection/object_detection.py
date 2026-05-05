import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load model
model = YOLO("yolov8n.pt")

# Initialize tracker
tracker = DeepSort(max_age=30)

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]

    detections = []

    # Get detections
    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        conf = float(box.conf[0])

        detections.append(([x1, y1, x2 - x1, y2 - y1], conf, 'object'))

    # Update tracker
    tracks = tracker.update_tracks(detections, frame=frame)

    # Draw tracking IDs
    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        l, t, w, h = track.to_ltrb()

        cv2.rectangle(frame, (int(l), int(t)), (int(w), int(h)), (0, 255, 0), 2)
        cv2.putText(frame, f"ID: {track_id}", (int(l), int(t)-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()