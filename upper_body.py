import SimpleCV as scv
import cv2,cv, numpy as np

import sys
def main():
    while 1:
        kinect = scv.Kinect()
        try:
            depth = kinect.getDepthMatrix()
            _,foreground = cv2.threshold(depth.astype(np.float32),int(sys.argv[1]),255,cv2.THRESH_BINARY)
            cv.ShowImage('Depth',cv.fromarray(np.array(foreground.astype(np.uint8))))
            cv.WaitKey(5)
        except KeyboardInterrupt:
            break
main()
