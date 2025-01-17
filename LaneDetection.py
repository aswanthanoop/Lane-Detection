# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located
    https://colab.research.google.com/drive/1YBVbTdoG5Sj-VWfUJFXb2or5KQ_yxzCo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('road.jpeg')

print(image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)



edges = cv2.Canny(blur, 50, 150)

height, width = image.shape[:2]
roi_vertices = [(0, height), (width/2, height/2), (width, height)]
mask_color = 255
mask = np.zeros_like(edges)
cv2.fillPoly(mask, np.array([roi_vertices], dtype=np.int32), mask_color)
masked_edges = cv2.bitwise_and(edges, mask)

lines = cv2.HoughLinesP(masked_edges, rho=6, theta=np.pi/60, threshold=160, minLineLength=40, maxLineGap=25)

line_image = np.zeros_like(image)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)

final_image = cv2.addWeighted(image, 0.8, line_image, 1, 0)

plt.imshow(final_image)

plt.show()

