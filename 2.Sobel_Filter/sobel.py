import cv2
import os

def apply_sobel(input_dir, output_dir):
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

            # Apply Sobel filter in x and y directions
            sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # Gradient in x
            sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # Gradient in y

            # Compute magnitude of gradients
            sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)

            # Normalize the result to 0-255 for visualization
            sobel_magnitude = cv2.convertScaleAbs(sobel_magnitude)

            # Save the output image
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, sobel_magnitude)
            print(f"Processed and saved Sobel filtered image: {output_path}")

def main():
    input_dir = "1.Gaussian_Filter/"
    output_dir = "2.Sobel_Filter/"
    apply_sobel(input_dir, output_dir)

if __name__ == "__main__":
    main()
