import os,sys
sys.path.append( os.path.abspath('../src') )

import core
import cv2

def test_segment_input_output_spec_check():
    img1= cv2.imread('../test/fixture/real_imgs/bw1.png')
    img2= cv2.imread('../test/fixture/real_imgs/bgr1.png')
    ret1= core.segmap(img1)
    ret2= core.segmap(img2)

    # look & feel
    cv2.imshow('img1',img1); cv2.imshow('img2',img2);
    cv2.imshow('ret1',ret1); cv2.imshow('ret2',ret2);
    cv2.waitKey(0)

# test different data(robustness)