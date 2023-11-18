import os

from ultralytics import YOLO
import cv2

# Web Cam's footage
cap = cv2.VideoCapture(0)

# Load a model
model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'best.pt')
model = YOLO(model_path)  # load a custom model

# Accuracy
threshold = 0.1

while True:
    ret, frame = cap.read()
    H, W, _ = frame.shape
    results = model(frame)[0]
    print("Frame Dimensions:", frame.shape)
    print("Number of Detections:", len(results.boxes.data.tolist()))

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('watch', frame)
    if cv2.waitKey(30) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
