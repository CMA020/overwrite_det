import cv2
import numpy as np

def adjust_levels(image, brightness=0, contrast=1, gamma=1):
    adjusted = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
    adjusted = np.power(adjusted / 255.0, gamma) * 255.0
    return adjusted

def on_brightness_change(value):
    global initial_brightness
    initial_brightness = value

def on_contrast_change(value):
    global initial_contrast
    initial_contrast = value

def on_gamma_change(value):
    global initial_gamma
    initial_gamma = value / 100.0

# Load the image
image = cv2.imread('Sample3.jpg')

# Initial parameters
initial_brightness = 0
initial_contrast = 100  # Multiply by 0.01 to get the actual contrast value
initial_gamma = 100.0  # Divide by 100 to get the actual gamma value

# Create a window to display the adjusted image
cv2.namedWindow('Adjusted Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Adjusted Image', 900, 900)

# Create sliders for adjusting brightness, contrast, and gamma
cv2.createTrackbar('Brightness', 'Adjusted Image', initial_brightness, 255, on_brightness_change)
cv2.createTrackbar('Contrast', 'Adjusted Image', initial_contrast, 200, on_contrast_change)
cv2.createTrackbar('Gamma', 'Adjusted Image', int(initial_gamma * 100), 200, on_gamma_change)

while True:
    adjusted_image = adjust_levels(image, initial_brightness, initial_contrast * 0.01, initial_gamma)
    cv2.imshow('Adjusted Image', adjusted_image)

    key = cv2.waitKey(1) & 0xFF

    # Exit the loop if the 'q' key is pressed
    if key == ord('q'):
        break

cv2.destroyAllWindows()