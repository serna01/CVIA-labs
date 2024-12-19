# Image Processing Pipeline

This script processes a series of images to compute and save grayscale, blurred, gradient, and gradient amplitude versions of each input image. It utilizes OpenCV and NumPy to perform the following operations:

1. Convert the image to grayscale.
2. Apply Gaussian blur.
3. Compute gradients in the x and y directions using Sobel filters.
4. Calculate the gradient amplitude.

The results are saved in corresponding subfolders (`gray`, `blur`, `sobelx`, `sobely`, and `Gamp`) within the same directory as the input images.

## Prerequisites

1. **Python 3.x**: Ensure you have Python installed on your system.
2. **Required Libraries**:
   - OpenCV: Install using `pip install opencv-python`
   - NumPy: Install using `pip install numpy`

## Directory Structure

Place your input images in a folder named `checkboard` (or another name as defined in the `path` variable). The directory structure should look like this:

```bash
python lab1b.py
```

```plaintext
lab_sessions_2024/
└── res/
    └── checkboard/
        ├── image1.jpg
        ├── image2.jpg
        ├── ...
        ├── gray/
        │   ├── image1.jpg
        │   ├── image2.jpg
        │   ├── ...
        ├── blur/
        │   ├── image1.jpg
        │   ├── image2.jpg
        │   ├── ...
        ├── sobelx/
        │   ├── image1.jpg
        │   ├── image2.jpg
        │   ├── ...
        ├── sobely/
        │   ├── image1.jpg
        │   ├── image2.jpg
        │   ├── ...
        └── Gamp/
            ├── image1.jpg
            ├── image2.jpg
            ├── ...

```
## Image Processing Steps

### Grayscale Conversion
Converts the input image to grayscale using OpenCV's `cv2.cvtColor`.

### Gaussian Blur
Applies a Gaussian blur with a kernel size of (5, 5) to reduce noise.

### Sobel Gradients
Computes gradients in the x and y directions using the Sobel operator (`cv2.Sobel`).

### Gradient Amplitude
Calculates the gradient magnitude (`Gamp`) using the formula:  
\[ Gamp = \sqrt{G_x^2 + G_y^2} \]

---

## Key Notes

### Edge Detection
Sobel filters calculate image gradients to highlight areas with high-intensity changes, which are often indicative of edges. The gradient magnitude combines x and y gradients to detect edges effectively.

### Output Quality
Ensure that the input images have adequate resolution to produce meaningful gradient computations.

---

## Troubleshooting

### If Images Are Not Saved:
- Ensure the `gray`, `blur`, `sobelx`, `sobely`, and `Gamp` directories exist or are writable.
- Check for permissions issues in the working directory.

### If Dependencies Are Missing:
- Install the required libraries as mentioned in the **Prerequisites** section.

---

## License
This script is free to use and modify for personal or educational purposes. For commercial use, please contact the author.

---

## Author
**Alejandro Serna Medina**  
For questions or support, feel free to contact: alejandro.serna.001@student.uni.lu
