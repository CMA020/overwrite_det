import cv2
import numpy as np

# Function to update the filtered image based on the neighborhood size
def update_filtered_image(neighborhood_size):
    kernel = np.ones((neighborhood_size, neighborhood_size), np.uint8)
    min_filtered_image = cv2.erode(original_image, kernel, iterations=1)
    resized_image = cv2.resize(min_filtered_image, (900, 900))
    cv2.imshow('Minimum Filtered Image', resized_image)

# Load the image
original_image = cv2.imread('Sample2.jpg')

# Create a window to display the filtered image
cv2.namedWindow('Minimum Filtered Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Minimum Filtered Image', 900, 900)

# Initial neighborhood size
neighborhood_size = 3

# Create a trackbar/slider to adjust the neighborhood size
cv2.createTrackbar('Neighborhood Size', 'Minimum Filtered Image', neighborhood_size, 21, update_filtered_image)

while True:
    key = cv2.waitKey(1) & 0xFF

    # Exit the loop if the 'q' key is pressed
    if key == ord('q'):
        break

cv2.destroyAllWindows()