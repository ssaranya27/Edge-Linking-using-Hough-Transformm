# Edge-Linking-using-Hough-Transform
## Aim:
To write a Python program to detect the lines using Hough Transform.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Import all the necessary modules for the program.

### Step2:
Load a image using imread() from cv2 module.

### Step3:
Convert the image to grayscale.

### Step4:
Using Canny operator from cv2,detect the edges of the image.

### Step5:
Using the HoughLinesP(),detect line co-ordinates for every points in the images.Using For loop,draw the lines on the found co-ordinates.Display the image.

## Program:
### Name : SARANYA S
### Reg.No: 212223220101
### Input image and grayscale image
```
import numpy as np
import cv2
import matplotlib.pyplot as plt

gray = cv2.imread('beaut.jpg', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('beaut.jpg', cv2.IMREAD_COLOR)
img_c = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
gray_rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

gray = cv2.GaussianBlur(gray, (3, 3), 0)

plt.figure(figsize=(13, 13))
plt.subplot(1, 2, 1)
plt.imshow(img_c)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(gray_rgb, cmap='gray')
plt.title("Gray Image")
plt.axis("off")
plt.show()
```
### Canny Edge detector output
```
canny = cv2.Canny(gray, 120, 150)

plt.imshow(canny, cmap='gray')
plt.title("Canny Edge Detector")
plt.axis("off")
plt.show()
```
### Display the result of Hough transform
```
lines = cv2.HoughLinesP(canny, 1, np.pi/180, threshold=80, minLineLength=50, maxLineGap=250)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img_c, (x1, y1), (x2, y2), (255, 0, 0), 3)

plt.imshow(img_c)
plt.title("Result Image")
plt.axis("off")
plt.show()
```
## Output:

### Input image and grayscale image
<img width="1248" height="415" alt="image" src="https://github.com/user-attachments/assets/7eb11539-4da4-4763-b8cc-d15c2fc3a75b" />

### Canny Edge detector output
<img width="665" height="471" alt="image" src="https://github.com/user-attachments/assets/95ca0f4e-e58d-48d9-94d2-bf4c1a62f803" />

### Display the result of Hough transform
<img width="667" height="461" alt="image" src="https://github.com/user-attachments/assets/3b33d2f6-8e58-443e-9915-23069327a3de" />

## Result:
Thus, the image has been successfully converted.
