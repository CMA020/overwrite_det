import cv2
import numpy as np

# Load the image
image = cv2.imread('Sample2.jpg')

# Create a copy of the image to apply the curves adjustment
curves_image = image.copy()

# Define the curve points as trackable values
curve_points = np.array([[0, 0], [100, 100], [200, 200], [255, 255]], np.uint8)

def update_curve_points(value):
    global curve_points
    for i in range(len(curve_points)):
        curve_points[i][1] = cv2.getTrackbarPos(f'Point {i + 1}', 'Curves Adjusted Image')
    apply_curves_adjustment()

def apply_curves_adjustment():
    for i in range(3):  # Apply to each channel (B, G, R)
        curves_image[:, :, i] = np.interp(image[:, :, i], curve_points[:, 0], curve_points[:, 1])
    cv2.imshow('Curves Adjusted Image', curves_image)

# Create a window to display the curves-adjusted image
cv2.namedWindow('Curves Adjusted Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Curves Adjusted Image', 900, 900)

# Create trackbars for each control point
for i in range(len(curve_points)):
    cv2.createTrackbar(f'Point {i + 1}', 'Curves Adjusted Image', curve_points[i][1], 255, update_curve_points)

# Apply the initial curves adjustment
apply_curves_adjustment()

while True:
    key = cv2.waitKey(1) & 0xFF

    # Exit the loop if the 'q' key is pressed
    if key == ord('q'):
        break

cv2.destroyAllWindows()