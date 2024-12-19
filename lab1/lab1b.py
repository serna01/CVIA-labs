import cv2 as cv
import glob
import os
import numpy as np

# Define the path to the images
path = '../lab_sessions_2024/res/checkboard/*.jpg'
print("Search path:", os.path.abspath(path))

# Load images
images = glob.glob(path)
print(len(images))

for fname in images:
    #read image from file
    img = cv.imread(fname)
    #convert image to grayscale------------------------------------------------------
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #save the grayscale image path
    save_path = os.path.join(os.path.dirname(fname), 'gray', os.path.basename(fname))
    #print("Saving to:", save_path)
    #save the grayscale image
    save = cv.imwrite(save_path, gray)
    
    #Apply gaussian blur to the grayscale image---------------------------------------
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    #save the blurred image path
    save_path = os.path.join(os.path.dirname(fname), 'blur', os.path.basename(fname))
    #print("Saving to:", save_path)
    #save the blurred image
    save = cv.imwrite(save_path, blur)
    
    #Compute Image Gradients in the x-Direction using Sobel----------------------------
    sobelx = cv.Sobel(blur, cv.CV_64F, 1, 0, ksize=3)
    #save the sobelx image path
    save_path = os.path.join(os.path.dirname(fname), 'sobelx', os.path.basename(fname))
    #save the sobelx image
    #print("Saving to:", save_path)
    save = cv.imwrite(save_path, sobelx)
    
    #Compute Image Gradients in the y-Direction using Sobel----------------------------
    sobely = cv.Sobel(blur, cv.CV_64F, 0, 1, ksize=3)
    #save the sobely image path
    save_path = os.path.join(os.path.dirname(fname), 'sobely', os.path.basename(fname))
    #save the sobely image
    #print("Saving to:", save_path)
    save = cv.imwrite(save_path, sobely)
    
    #calculate the gradient amplitude image Gamp = sqrt(Gx^2 + Gy^2)-------------------
    #convert images into numpy arrays
    sobelx = np.array(sobelx)
    sobely = np.array(sobely)
    #compute the gradient amplitude image
    Gamp = np.sqrt(sobelx**2 + sobely**2)
    #save the gradient amplitude image path
    save_path = os.path.join(os.path.dirname(fname), 'Gamp', os.path.basename(fname))   
    #save the gradient amplitude image
    #print("Saving to:", save_path)
    save = cv.imwrite(save_path, Gamp)
    
    #Briefly describe how calculating gradients using Sobel filters aids in edge detection:
        #Sobel filters are used to calculate the first derivative of the image in the x and y directions.
        #The gradient magnitude is calculated by taking the square root of the sum of the squares of the x and y gradients.
        #With this magnitude calculation we get a sense of the intensity of the edges in the image, meaning where the x and y gradients are high,
        #the gradient magnitude will be high.
        #Thus these are used to detect edges in the image.