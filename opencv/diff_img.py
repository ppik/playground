#!/usr/lib/python2
# A simple script to display difference of two consequent frames
# grabbed from webcam.

import cv2
import numpy as np
import sys
import time

EXIT_KEYS = [27, ord('q'), ord('Q')]    # Esc, q, Q

def get_frame(cam, gray=False, dtype='uint8'):
    """
    Gets frame from VideoCapture object. If gray is set to True,
    then converts the frame to grayscale before returning it.
    """

    _, frame = cam.read()

    if gray:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame = frame.astype(dtype)

    return frame

def calc_diff(frame0, frame1):
    """
    Calculates the difference image between two frames.
    """
    im = frame1 - frame0
    im = im/2./255. # Scaling
    im += 0.5   # Shift the no change to gray value.
    
    return im

def diff_img(gray = False):
    # Initialize camera
    cam = cv2.VideoCapture(0)

    # Get the first frame
    frame = get_frame(cam, gray=gray, dtype='int16')
    # For calculating effective framerate
    toc = time.time()

    # Display frame-by-frame until Esc, q, or Q is pressed
    while True:
        prev_frame = frame
        tic = toc
        
        frame = get_frame(cam, gray=gray, dtype='int16')
        toc = time.time()
        fps = 1./(toc - tic)
        
        im = calc_diff(prev_frame, frame)
        cv2.putText(im, '{:4.1f} fps'.format(fps), (5,15),
                    cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
        
        cv2.imshow('frame', im)

        if cv2.waitKey(1) & 0xFF in EXIT_KEYS:
            break
    
    # Done, relese the capture
    cam.release()
    cv2.destroyAllWindows()


def main(argv):
    # Parse arguments and run the actual function that does the work.
    if '-g' in argv:
        gray = True
    else:
        gray = False
    
    diff_img(gray=gray)


if __name__ == '__main__':
    main(sys.argv[1:])
