import cv2
from ultralytics import YOLO
from fpga_detector import fpga_process

model = YOLO("yolov8m.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # FPGA preprocessing
    fpga_process(frame)

    # YOLO detection
    results = model(frame)

    annotated = results[0].plot()

    cv2.imshow("ARM+FPGA Object Detection", annotated)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()
