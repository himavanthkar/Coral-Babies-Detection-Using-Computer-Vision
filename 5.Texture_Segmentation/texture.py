import cv2
import numpy as np
import os
from sklearn.cluster import KMeans

def create_laws_kernels():
    """Create 1D Law's texture energy kernels."""
    L5 = np.array([1, 4, 6, 4, 1])  # Level
    E5 = np.array([-1, -2, 0, 2, 1])  # Edge
    S5 = np.array([-1, 0, 2, 0, -1])  # Spot
    R5 = np.array([1, -4, 6, -4, 1])  # Ripple
    W5 = np.array([-1, 2, 0, -2, 1])  # Wave
    return [L5, E5, S5, R5, W5]

def compute_texture_features(image, kernels):
    """Apply 1D Law's filters to extract texture features."""
    features = []
    for kernel in kernels:
        # Convolve horizontally
        horizontal_response = cv2.filter2D(image, -1, kernel[np.newaxis, :])
        # Convolve vertically
        vertical_response = cv2.filter2D(image, -1, kernel[:, np.newaxis])
        # Combine responses
        energy = np.abs(horizontal_response) + np.abs(vertical_response)
        features.append(energy)
    return np.stack(features, axis=-1)  # Stack into a feature vector

def assign_colors_to_clusters(cluster_labels, height, width):
    """Assign unique colors to each cluster label."""
    # Map each cluster to a random color
    unique_labels = np.unique(cluster_labels)
    colors = np.random.randint(0, 255, (len(unique_labels), 3), dtype=np.uint8)
    colored_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Assign colors to each pixel based on its cluster label
    for label, color in zip(unique_labels, colors):
        colored_image[cluster_labels == label] = color

    return colored_image

def texture_segmentation(input_dir, output_dir, n_clusters=5, blur_kernel_size=(15, 15)):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    kernels = create_laws_kernels()  # Generate 1D Law's kernels

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_image_path = os.path.join(input_dir, filename)
            output_image_path = os.path.join(output_dir, f"segmented_{filename}")

            # Load the image
            img = cv2.imread(input_image_path)
            if img is None:
                print(f"Failed to load image: {filename}")
                continue

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Apply Gaussian blur to smooth fine details
            blurred_gray = cv2.GaussianBlur(gray, blur_kernel_size, 0)

            # Compute texture features
            texture_features = compute_texture_features(blurred_gray, kernels)

            # Flatten texture features into a feature vector
            feature_vector = texture_features.reshape((-1, texture_features.shape[-1]))

            # Perform K-Means clustering
            kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(feature_vector)
            cluster_labels = kmeans.labels_.reshape(gray.shape)

            # Create a color image based on the cluster labels
            colored_segmented_image = assign_colors_to_clusters(cluster_labels, gray.shape[0], gray.shape[1])

            # Save the segmented image
            cv2.imwrite(output_image_path, colored_segmented_image)
            print(f"Segmented image saved to: {output_image_path}")

if __name__ == "__main__":
    # Input and output directories
    input_dir = "original_images/"
    output_dir = "5.Texture_Segmentation/"
    texture_segmentation(input_dir, output_dir, n_clusters=5, blur_kernel_size=(15, 15))
