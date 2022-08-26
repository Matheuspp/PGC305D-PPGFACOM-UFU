#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 26/08/2022 01:41

@author: Matheus Silva
"""

# ### built-in deps
# ### external deps
import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_img(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return img

def convert_to_vector(img):
    pass

def main(path):
    image = read_img(path)
    # ### squeeze image
    img = np.squeeze(image)

    plt.hist(img, bins=range(np.max(img)+1))
    plt.show()
    

if __name__ == '__main__':
    path = 'test_hist.jpeg'
    main(path)
