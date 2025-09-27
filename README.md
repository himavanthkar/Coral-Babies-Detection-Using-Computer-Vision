
# Coral Babies Detection Using Computer Vision Techniques

This project focuses on the detection and analysis of coral larvae (coral babies) using various computer vision techniques, including preprocessing, edge detection, segmentation, and shape-based detection.

---

## **Overview**

The goal of this project is to analyze images of coral samples and detect coral babies. Through preprocessing, edge detection, and shape-based transformations, we aim to accurately identify and study coral larvae. This work highlights the importance of selecting the right combination of image processing techniques to achieve optimal results.

---

## **Techniques Used**

1. **Image Filtering**
   - Used **Gaussian Filtering** to reduce noise and improve image quality.
   - Enhanced image sharpness by smoothing while preserving edges.

2. **Edge Detection**
   - Compared and implemented algorithms like **Sobel**, **Canny**, and **Laplacian** filters to identify edges.
   - Selected the most effective method for further steps based on results.

3. **Thresholding and Contour Detection**
   - Applied thresholding to segment the image by intensity differences.
   - Used contours to highlight regions of interest and identify coral larvae.

4. **Hough Transform**
   - Leveraged Hough Transform to detect circular patterns, representing coral babies.
   - Improved detection accuracy by refining parameters and incorporating contour filtering.

5. **Future Work**
   - Explore machine learning models for classification and age prediction of coral larvae.
   - Implement segmentation based on texture and other advanced techniques.

---

## **Features**

- **Thresholding:** Identifies darker spots (coral babies) based on pixel intensity.
- **Contour Detection:** Highlights edges and regions of interest in red.
- **Circle Detection:** Uses the Hough Transform for identifying circular structures in images.

---

## **Project Workflow**

1. **Image Preprocessing**
   - Load coral images.
   - Apply Gaussian filters for noise reduction.

2. **Edge Detection**
   - Experiment with Sobel, Canny, and Laplacian filters.
   - Select the best-performing algorithm for edge highlighting.

3. **Thresholding and Contours**
   - Use thresholding to extract dark spots.
   - Detect and draw contours to localize coral larvae.

4. **Hough Transform**
   - Apply Hough Transform to detect circles.
   - Tune parameters for optimal results.

5. **Analysis and Comparison**
   - Compare edge detection methods and circle-detection techniques.
   - Evaluate results to refine the detection pipeline.

---

## **Setup and Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/username/coral-babies-detection.git
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the preprocessing and detection scripts:
   ```bash
   python gaussian.py
   python sobel.py
   python hough.py
   ```

4. View the results in the output folder.

---

## **Directory Structure**

```plaintext
coral-babies-detection/
│
├── images/                  # Input coral images
├── outputs/                 # Generated output images
├── gaussian.py              # Code for Gaussian Filtering
├── sobel.py                 # Code for Sobel edge detection
├── hough.py                 # Code for Hough Transform
├── README.md                # Project documentation
├── requirements.txt         # Dependencies
└── Presentation.pptx        # Final project presentation
```

---

## **Results**

The project produced the following results:
- Enhanced images after Gaussian filtering.
- Clearer edges using Sobel, Canny, and Laplacian filters.
- Coral babies detected using thresholding, contouring, and Hough Transform.

---

## **Future Scope**

- Experiment with texture-based segmentation.
- Train machine learning models for classification tasks.
- Analyze coral baby clusters based on size, quantity, and patterns.

---

## **Contributors**

- **Anaya Dandekar**
- **Himavanth Karpurapu**
- **Sanjana Nagwekar**

---

## **License**



---

## **Acknowledgments**

Special thanks to Professor Nada for guidance and support throughout the project.
