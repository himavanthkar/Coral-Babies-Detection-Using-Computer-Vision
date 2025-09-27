'''
# ODD NUMBERED IMAGES

import cv2
import numpy as np
import matplotlib.pyplot as plt
# from google.colab.patches import cv2_imshow

img = cv2.imread('original_images/35_T2_5_timepoint1.JPG')

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not open or read the image.")
else:
    # Convert to grayscale
    img[np.all(img < 40, axis=2)] = 255
    cv2.imwrite('6.Connected_Components/debugging_steps/bg_35_T2_5_timepoint1.JPG', img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    edges = cv2.Canny(gray, 50, 150)
    cv2.imwrite('6.Connected_Components/debugging_steps/edges_35_T2_5_timepoint1.JPG', edges)

    # Morphological operations
    kernel = np.ones((5, 5), np.uint8)
    result = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=2)
    dilated = cv2.dilate(result, kernel, iterations=1)
    result2 = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel, iterations=3)
    cv2.imwrite('6.Connected_Components/debugging_steps/morph_35_T2_5_timepoint1.JPG', result2)
    result2 = cv2.bitwise_not(result2)

    # Connected components
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(result2, 8, cv2.CV_32S)

    # Define area thresholds
    a = 10000
    b = 100000

    # Create a mask for components within the area range
    mask = np.zeros_like(result2, dtype=np.uint8)
    for i in range(1, num_labels):  # Iterate through components (excluding background)
        area = stats[i, cv2.CC_STAT_AREA]
        if a < area < b:
            component_mask = (labels == i).astype(np.uint8) * 255
            mask = cv2.bitwise_or(mask, component_mask)
    mask = cv2.dilate(mask, kernel, iterations=5)

    # Display the mask
    cv2.imwrite('6.Connected_Components/debugging_steps/mask_35_T2_5_timepoint1.JPG', mask)
    img2 = cv2.imread('original_images/35_T2_5_timepoint1.JPG')

    # Masked image
    masked_img = cv2.bitwise_and(img2, img2, mask=mask)
    cv2.imwrite('6.Connected_Components/debugging_steps/ImgMask_35_T2_5_timepoint1.JPG', masked_img)

    # Hough Circle Transform
    image = masked_img
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    circles_refined = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=200,
        param1=50,
        param2=25,
        minRadius=80,
        maxRadius=100
    )

    # Draw the detected circles
    output_refined = image.copy()
    circle_count = 0  
    if circles_refined is not None:
        circles_refined = np.uint16(np.around(circles_refined))
        circle_count = len(circles_refined[0])  
        for circle in circles_refined[0, :]:
            # Draw the outer circle
            cv2.circle(output_refined, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(output_refined, (circle[0], circle[1]), 2, (0, 0, 255), 3)

            # Drawing outer circle and center on original img
            cv2.circle(img2, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
            cv2.circle(img2, (circle[0], circle[1]), 2, (0, 0, 255), 3)

    # Save the final output with circles drawn 
    cv2.imwrite('6.Connected_Components/debugging_steps/circles_35_T2_5_timepoint1.JPG', output_refined)
    cv2.imwrite('6.Connected_Components/result_35_T2_5_timepoint1.JPG', img2)
    print(f"Number of coral larvae detected: {circle_count}")
'''

##########################################################################################################

# EVEN NUMBERED IMAGES

import cv2
import numpy as np
import matplotlib.pyplot as plt
# from google.colab.patches import cv2_imshow

# Load the image (replace 'image.jpg' with your image path)
img = cv2.imread('original_images/35_T2_5_timepoint0.JPG')

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not open or read the image.")
else:
    # # Turn black bg to white
    # img[np.all(img < 40, axis=2)] = 255
    # cv2_imshow(img)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # # Apply Gaussian blur and canny edge detection
    # edges = cv2.Canny(gray, 70, 150)
    # cv2_imshow(edges)

    # Apply thresholding to isolate dark circles
    # Use cv2.THRESH_BINARY_INV to make dark regions black and light regions white
    _, thresholded = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite('6.Connected_Components/debugging_steps/debugging_steps_0/thresh_35_T2_5_timepoint0.JPG', thresholded)

    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(thresholded, kernel, iterations=1)
    cv2.imwrite('6.Connected_Components/debugging_steps/debugging_steps_0/dilated_35_T2_5_timepoint0.JPG', dilated)

    # Apply morphological operations to remove noise and fill gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    processed = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)

    # Step 4: Optional - Invert again if needed to make background white
    processed = cv2.bitwise_not(processed)

    # Display the result
    cv2.imwrite('6.Connected_Components/debugging_steps/debugging_steps_0/processed_35_T2_5_timepoint0.JPG', processed)

    # Morphological operations
    result = cv2.morphologyEx(processed, cv2.MORPH_CLOSE, kernel, iterations=2)
    # dilated = cv2.dilate(result, kernel, iterations=1)
    result2 = cv2.morphologyEx(result, cv2.MORPH_CLOSE, kernel, iterations=3)
    cv2.imwrite('6.Connected_Components/debugging_steps/debugging_steps_0/morph_35_T2_5_timepoint0.JPG', result2)
    result2 = cv2.bitwise_not(result2)
    

    # Connected components
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(result2, 8, cv2.CV_32S)

    # Define area thresholds
    a = 10000
    b = 100000

    # Create a mask for components within the area range
    mask = np.zeros_like(result2, dtype=np.uint8)
    for i in range(1, num_labels):  # Iterate through components (excluding background)
        area = stats[i, cv2.CC_STAT_AREA]
        if a < area < b:
            component_mask = (labels == i).astype(np.uint8) * 255
            mask = cv2.bitwise_or(mask, component_mask)
    mask = cv2.dilate(mask, kernel, iterations=5)

    # Display the mask
    cv2.imwrite('6.Connected_Components/debugging_steps/debugging_steps_0/mask_35_T2_5_timepoint0.JPG', mask)
    img2 = cv2.imread('original_images/35_T2_5_timepoint0.JPG')

    # Masked image
    masked_img = cv2.bitwise_and(img2, img2, mask=mask)
    cv2.imwrite('6.Connected_Components/debugging_steps/debugging_steps_0/ImgMask_35_T2_5_timepoint0.JPG', masked_img)

    # Hough Circle Transform
    image = masked_img
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    circles_refined = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=100,
        param1=50,
        param2=25,
        minRadius=20,
        maxRadius=60
    )

    # Draw the detected circles
    output_refined = image.copy()
    circle_count = 0  
    if circles_refined is not None:
        circles_refined = np.uint16(np.around(circles_refined))
        circle_count = len(circles_refined[0])  
        for circle in circles_refined[0, :]:
            # Draw the outer circle
            cv2.circle(output_refined, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(output_refined, (circle[0], circle[1]), 2, (0, 0, 255), 3)

            # Drawing outer circle and center on original img
            cv2.circle(img2, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
            cv2.circle(img2, (circle[0], circle[1]), 2, (0, 0, 255), 3)

    # Save the final output with circles drawn
    cv2.imwrite('6.Connected_Components/debugging_steps/debugging_steps_0/circles_35_T2_5_timepoint0.JPG', output_refined)
    cv2.imwrite('6.Connected_Components/result_35_T2_5_timepoint0.JPG', img2)
    print(f"Number of coral larvae detected: {circle_count}")