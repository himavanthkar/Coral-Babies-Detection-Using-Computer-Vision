import cv2
import os

def main():
    input_dir = "original_images/"
    output_dir = "1.Gaussian_Filter/"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".jpg"):
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path, cv2.IMREAD_COLOR)

            if img is None:
                print(f"Failed to load image: {filename}")
                continue

            # Apply Gaussian blur with larger kernel size and sigma
            blurred = cv2.GaussianBlur(img, (15, 15), 10)

            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, blurred)
            print(f"Processed and saved: {output_path}")

if __name__ == "__main__":
    main()
