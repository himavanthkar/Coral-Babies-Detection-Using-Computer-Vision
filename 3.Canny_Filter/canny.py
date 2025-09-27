import cv2
import os

def apply_canny(input_dir, output_dir, lower_threshold, upper_threshold):
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

            # Apply Canny edge detection
            edges = cv2.Canny(gray, lower_threshold, upper_threshold)

            # Save the output image
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, edges)
            print(f"Processed and saved Canny filtered image: {output_path}")

def main():
    input_dir = "1.Gaussian_Filter/"
    output_dir = "2.Canny_Filter/"

    # Set thresholds for Canny edge detection
    lower_threshold = 10
    upper_threshold = 35

    apply_canny(input_dir, output_dir, lower_threshold, upper_threshold)

if __name__ == "__main__":
    main()
