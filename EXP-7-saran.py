#!/usr/bin/env python
# coding: utf-8

# In[5]:


# NAME : SARANYA S
# Reg.No: 212223220101


# In[6]:


import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[7]:


gray = cv2.imread('nature.jpg', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('nature.jpg', cv2.IMREAD_COLOR)
img_c = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
gray_rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)


# In[8]:


gray = cv2.GaussianBlur(gray, (3, 3), 0)


# In[9]:


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


# In[10]:


canny = cv2.Canny(gray, 120, 150)

plt.imshow(canny, cmap='gray')
plt.title("Canny Edge Detector")
plt.axis("off")
plt.show()


# In[11]:


lines = cv2.HoughLinesP(canny, 1, np.pi/180, threshold=80, minLineLength=50, maxLineGap=250)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img_c, (x1, y1), (x2, y2), (255, 0, 0), 3)

plt.imshow(img_c)
plt.title("Result Image")
plt.axis("off")
plt.show()


# In[ ]:




