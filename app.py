import cv2
import numpy as np

# Load the image of the leaf
img = cv2.imread('11.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a threshold to the image to separate the background from the leaf
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Apply a morphological operation to fill any gaps in the leaf's veins
kernel = np.ones((3,3), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Find the contours of the leaf
contours, hierarchy = cv2.findContours(morph, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Calculate the total area of the leaf
leaf_area = img.shape[0] * img.shape[1]

# Calculate the area of the non-green regions
non_green_area = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100:  # filter out small contours that are not significant
        non_green_area += area

# Calculate the ratio of non-green area to leaf area
ratio = non_green_area / leaf_area
print("Non-green area ratio:", ratio)


import cv2
import numpy as np

# Read the image
img2 = cv2.imread('11.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Apply a threshold to the image
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]

# Find the contours in the image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Calculate the area of the largest contour, which corresponds to the foreground
foreground_area = max([cv2.contourArea(c) for c in contours])

# Calculate the total area of the image
total_area = img2.shape[0] * img2.shape[1]

# Calculate the background area
background_area = total_area - foreground_area

# Calculate the background ratio
background_ratio = background_area / total_area



if(ratio-background_ratio>0.4):
    print("plant is highly diseased");
else:
    print("plant is in early stages of disease");
