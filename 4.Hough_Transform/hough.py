'''
# METHOD 1

import cv2
import os
import numpy as np

def detect_coral_babies(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".jpg"):
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path, cv2.IMREAD_COLOR)
            if img is None:
                print(f"Failed to load image: {filename}")
                continue

            # Convert the image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Apply Gaussian blur to smooth the image and reduce noise
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)

            # Apply adaptive thresholding to binarize the image
            thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

            # Find contours in the binary image
            contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # Filter the contours to find the ones with an approximate circular shape
            coral_babies = []
            for cnt in contours:
                area = cv2.contourArea(cnt)
                perimeter = cv2.arcLength(cnt, True)
                if perimeter > 0:
                    circularity = 4 * np.pi * area / (perimeter ** 2)
                    if 0.5 <= circularity <= 0.9:
                        coral_babies.append(cnt)

            # Draw the detected coral babies on the original image
            output_img = img.copy()
            for cnt in coral_babies:
                (x, y), radius = cv2.minEnclosingCircle(cnt)
                center = (int(x), int(y))
                radius = int(radius)
                cv2.circle(output_img, center, radius, (0, 255, 0), 2)

            # Save the output image with detected coral babies
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, output_img)
            print(f"Processed and saved image with {len(coral_babies)} coral babies detected: {output_path}")

def main():
    input_dir = "original_images/"
    output_dir = "4.Hough_Transform/"
    detect_coral_babies(input_dir, output_dir)

if __name__ == "__main__":
    main()
'''
###########################################################################################################################
'''
# METHOD 2

import cv2
import os
import numpy as np

def detect_coral_babies(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".jpg"):
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path, cv2.IMREAD_COLOR)
            if img is None:
                print(f"Failed to load image: {filename}")
                continue

            # Convert the image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Apply Gaussian blur to smooth the image and reduce noise
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)

            # Apply adaptive thresholding to binarize the image
            thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

            # Find contours in the binary image
            contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # Filter the contours to find the ones with an approximate circular shape
            coral_babies = []
            for cnt in contours:
                area = cv2.contourArea(cnt)
                perimeter = cv2.arcLength(cnt, True)
                if 20 < perimeter < 5000 and 50 < area < 20000:
                    circularity = 4 * np.pi * area / (perimeter ** 2)
                    if 0.5 <= circularity <= 0.9:
                        coral_babies.append(cnt)

            # Draw the detected coral babies on the original image
            output_img = img.copy()
            for cnt in coral_babies:
                (x, y), radius = cv2.minEnclosingCircle(cnt)
                center = (int(x), int(y))
                radius = int(radius)
                cv2.circle(output_img, center, radius, (0, 255, 0), 2)

            # Save the output image with detected coral babies
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, output_img)
            print(f"Processed and saved image with {len(coral_babies)} coral babies detected: {output_path}")

def main():
    input_dir = "original_images/"
    output_dir = "4.Hough_Transform/"
    detect_coral_babies(input_dir, output_dir)

if __name__ == "__main__":
    main()
'''
###########################################################################################################################
'''
# METHOD 3

import cv2
import numpy as np

# Load the image
image = cv2.imread('original_images/32_T2_6_timepoint0.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and improve circle detection
blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Use HoughCircles to detect circles in the image
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=20,
                           param1=50, param2=30, minRadius=50, maxRadius=100)

# If some circles are detected, let's draw them on the original image
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    # Print the number of detected coral babies
    print(f"Number of detected coral babies: {len(circles)}")

# Save the result image
cv2.imwrite('4.Hough_Transform/new1.jpg', image)

print("The image with detected coral babies has been saved as 'coral_babies_detected.jpg'.")

'''
###########################################################################################################################

# METHOD 4

from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Load the image
image_path = "original_images/tahoe.JPG"
image = Image.open(image_path)

# Convert image to grayscale for easier processing
image_cv = cv2.imread(image_path)
gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

# Use HoughCircles to detect circular shapes
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=55,
    param1=50,
    param2=35,
    minRadius=60,
    maxRadius=80
)

# Create a copy of the image to draw the detections
output_image = image.copy()
draw = ImageDraw.Draw(output_image)
detected_count = 0

# Draw detected circles on the image
if circles is not None:
    circles = np.uint16(np.around(circles))
    detected_count = circles.shape[1]
    for i in circles[0, :]:
        # Validate coordinates to avoid overflow
        x0, y0 = max(i[0] - i[2], 0), max(i[1] - i[2], 0)  # Top-left corner
        x1, y1 = min(i[0] + i[2], image.width), min(i[1] + i[2], image.height)  # Bottom-right corner

        # Only draw if the coordinates are valid
        if x1 > x0 and y1 > y0:
            draw.ellipse(
                [(x0, y0), (x1, y1)],
                outline="red",
                width=5
            )

# Save the output image as JPG
output_image.convert("RGB").save('4.Hough_Transform/tahoe.JPG', "JPEG")
print(f"Circles detected: {detected_count}")

# Show the result and detected count
plt.figure(figsize=(8, 8))
plt.imshow(output_image)
plt.axis("off")
plt.title(f"Detected Coral Larvae: {detected_count}")
plt.show()

###########################################################################################################################
'''
# METHOD 5

import cv2
import numpy as np
import os

def detect_and_circle_white_spots(input_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_image_path = os.path.join(input_dir, filename)
            output_image_path = os.path.join(output_dir, filename)

            # Load the image
            img = cv2.imread(input_image_path)
            if img is None:
                print(f"Failed to load image: {filename}")
                continue

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Preprocess: Apply GaussianBlur to reduce noise
            gray_blurred = cv2.GaussianBlur(gray, (15, 15), 2)

            # Adaptive thresholding with stricter parameters
            thresholded = cv2.adaptiveThreshold(
                gray_blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5
            )

            # Apply morphological operations to clean up small details
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6, 6))
            thresholded = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)

            # Debug: Save the thresholded image
            debug_threshold_path = os.path.join(output_dir, f"thresholded_{filename}")
            cv2.imwrite(debug_threshold_path, thresholded)
            print(f"Saved thresholded image: {debug_threshold_path}")
            
            # Dilate the image
            dilation_kernel= np.ones((7,7),np.uint8)
            debug_dilated_path = os.path.join(output_dir, f"dilated_{filename}")
            dilated_image = cv2.dilate(thresholded, dilation_kernel, iterations=2)
            cv2.imwrite(debug_dilated_path, dilated_image)

            # Inverting image
            debug_inverted_path = os.path.join(output_dir, f"inverted_{filename}")
            inverted_image = cv2.bitwise_not(dilated_image)
            cv2.imwrite(debug_inverted_path, inverted_image)

            # More preprcessing- apply thresholding and morphological operations for enhancement, noise removal and better separation of white spots
            # thresholded2 = cv2.adaptiveThreshold(inverted_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, -2)
            # kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
            # processed = cv2.morphologyEx(inverted_image, cv2.MORPH_OPEN, kernel2, iterations=2)
            # debug_processed_path = os.path.join(output_dir, f"processed{filename}")
            # cv2.imwrite(debug_processed_path, processed)
            processed = cv2.GaussianBlur(inverted_image, (41, 41), 2)
            debug_processed_path = os.path.join(output_dir, f"processed{filename}")
            cv2.imwrite(debug_processed_path, processed)

            # Find contours in the cleaned thresholded image
            contours, _ = cv2.findContours(processed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(contours) == 0:
                print(f"No contours detected in {filename}.")
                continue

            # Debug: Draw contours on a copy of the original image
            debug_contours_img = img.copy()
            cv2.drawContours(debug_contours_img, contours, -1, (0, 0, 255), 1)
            debug_contours_path = os.path.join(output_dir, f"contours_{filename}")
            cv2.imwrite(debug_contours_path, debug_contours_img)
            print(len(contours))

            # Filter contours by area
            filtered_contours = []
            for contour in contours:
                area = cv2.contourArea(contour)
                if 100 <= area <= 500:
                    filtered_contours.append(contour)

            # Draw filtered contours on the original image
            filtered_cont = img.copy()
            cv2.drawContours(filtered_cont, filtered_contours, -1, (0, 255, 0), 2)

            debug_filt_contours_path = os.path.join(output_dir, f"filt_contours_{filename}")
            cv2.imwrite(debug_filt_contours_path, filtered_cont)
            print(f"Saved filtered contours image: {debug_filt_contours_path}")

            # Draw filtered contours on black background
            # Create a blank black image of the same size as the input image
            black_background = np.zeros_like(img)
            # Draw the filtered contours on the black background
            cv2.drawContours(black_background, filtered_contours, -1, (0, 255, 0), 2)
            black_bg_path = os.path.join(output_dir, f"black_bg_{filename}")
            cv2.imwrite(black_bg_path, black_background)
            print(f"Saved filtered contours image: {black_bg_path}")



            # Draw circles around each white spot
            for filtered_contour in filtered_contours:
                # Calculate the minimum enclosing circle
                (x, y), radius = cv2.minEnclosingCircle(filtered_contour)
                center = (int(x), int(y))
                radius = int(radius)

                # Draw the circle on the original image
                if radius > 5:  # Filter out very small circles
                    cv2.circle(img, center, radius, (0, 255, 0), 2)  # Green circle

            # Save the output image with drawn circles
            cv2.imwrite(output_image_path, img)
            print(f"Output saved to: {output_image_path}")

if __name__ == "__main__":
    # Input and output directories
    input_dir = "original_images/"  # Replace with the path to your input folder
    output_dir = "trial/"  # Replace with the path to your output folder

    # Run the detection
    trial_img=cv2.imread('original_images/32_T2_6_timepoint1.JPG')
    print(trial_img.shape)
    detect_and_circle_white_spots(input_dir, output_dir)
'''
##############################################################################################
'''
# METHOD 6

import cv2
import numpy as np
import os

def detect_and_circle_dark_spots(input_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_image_path = os.path.join(input_dir, filename)
            output_image_path = os.path.join(output_dir, filename)

            # Load the image
            img = cv2.imread(input_image_path)
            if img is None:
                print(f"Failed to load image: {filename}")
                continue

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Preprocess: Apply GaussianBlur to reduce noise
            gray_blurred = cv2.GaussianBlur(gray, (15, 15), 2)

            # Adaptive thresholding to detect dark spots
            thresholded = cv2.adaptiveThreshold(
                gray_blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 5
            )

            # Apply morphological operations to clean up small details
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6, 6))
            thresholded = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)

            # Debug: Save the thresholded image
            debug_threshold_path = os.path.join(output_dir, f"thresholded_{filename}")
            cv2.imwrite(debug_threshold_path, thresholded)
            print(f"Saved thresholded image: {debug_threshold_path}")

            # Find contours in the cleaned thresholded image
            contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(contours) == 0:
                print(f"No contours detected in {filename}.")
                continue

            # Debug: Draw contours on a copy of the original image
            debug_contours_img = img.copy()
            cv2.drawContours(debug_contours_img, contours, -1, (0, 0, 255), 1)
            debug_contours_path = os.path.join(output_dir, f"contours_{filename}")
            cv2.imwrite(debug_contours_path, debug_contours_img)
            print(f"Saved contours image: {debug_contours_path}")

            # Draw circles around each dark spot
            for contour in contours:
                # Calculate the minimum enclosing circle
                (x, y), radius = cv2.minEnclosingCircle(contour)
                center = (int(x), int(y))
                radius = int(radius)

                # Draw the circle on the original image
                if radius > 5:  # Filter out very small circles
                    cv2.circle(img, center, radius, (0, 255, 0), 2)  # Green circle

            # Save the output image with drawn circles
            cv2.imwrite(output_image_path, img)
            print(f"Output saved to: {output_image_path}")

if __name__ == "__main__":
    # Input and output directories
    input_dir = "original_images/"  # Replace with the path to your input folder
    output_dir = "4.Dark_Spots_Circled/"  # Replace with the path to your output folder

    # Run the detection
    detect_and_circle_dark_spots(input_dir, output_dir)
'''