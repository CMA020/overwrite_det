from ultralytics import YOLO
import os
import cv2

model = YOLO(os.path.expanduser('~/overwrite_det/last_20_OWO.pt'))

def pred(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bgr_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    img = cv2.resize(img, (2048, 2048))
    bgr_image = cv2.resize(bgr_image, (2048, 2048))
    model.predict(bgr_image, save=True, show=True, imgsz=(2048, 2048))
    results = model(bgr_image, imgsz=(2048, 2048),conf=0.55)


    for result in results:
        boxes = result.boxes  # Boxes object for bbox outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs

        for box in boxes:
            x = int(box.xywh[0][0])
            y = int(box.xywh[0][1])
            w = int(box.xywh[0][2])
            h = int(box.xywh[0][3])

            cv2.rectangle(img, (x - int(w / 2), y - int(h / 2)), ((x + int(w / 2)), (y + int(h / 2))),
                          (0, 0, 255),
                          thickness=4)


    return img


if __name__ == '__main__':
    while True:
        image = cv2.imread("Sample2.jpg")
        #image=cv2.imread("Sample2.jpg")
        # Create an instance of the CLAHE (Contrast Limited Adaptive Histogram Equalization) class
        final=pred(image)
        cv2.imwrite("final.jpg",final)

