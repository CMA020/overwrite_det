import cv2

# Function to update the binary image based on the threshold value
def update_binary_image(threshold_value):
    _, binary_image = cv2.threshold(original_image, threshold_value, 255, cv2.THRESH_BINARY)
    resized_image = cv2.resize(binary_image, (900, 900))
    cv2.imshow('Binary Image', resized_image)

# Load the image
original_image = cv2.imread('Sample5.jpg', cv2.IMREAD_GRAYSCALE)

# Initial threshold value
threshold_value = 100

# Create a window to display the binary image
cv2.namedWindow('Binary Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Binary Image', 900, 900)

# Create a trackbar/slider to adjust the threshold value
cv2.createTrackbar('Threshold', 'Binary Image', threshold_value, 255, update_binary_image)

while True:
    key = cv2.waitKey(1) & 0xFF

    # Exit the loop if the 'q' key is pressed
    if key == ord('q'):
        break

cv2.destroyAllWindows()
