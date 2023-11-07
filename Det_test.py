from ultralytics import YOLO
import os
import cv2

model = YOLO(os.path.expanduser('~/overwrite_det/best_17_O.pt'))
clip_limit = 78  # Set your desired clip limit (78 in this example)
tile_size = 20


if __name__ == '__main__':
    while True:
        image = cv2.imread("Sample3.jpg", cv2.IMREAD_GRAYSCALE)
        #image=cv2.imread("Sample2.jpg")
        # Create an instance of the CLAHE (Contrast Limited Adaptive Histogram Equalization) class

        bgr_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        model.predict(bgr_image, save=True, show=True)
        cv2.waitKey(1)

