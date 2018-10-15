import cv2
import numpy as np

class Drawer():

    def __init__(self, magnify=False):
        cv2.namedWindow("strategies")
        cv2.namedWindow("reputations")
        cv2.namedWindow("totals")
        self.magnify = magnify

    def draw(self, img, _type="strategies", norm=False):
        if norm:
            _max, _min = np.amax(img), np.amin(img)
            if _max > 0.0:
                img = np.divide(img, _max)
        if not self.magnify:
            cv2.imshow(_type, img)
        else:
            cv2.imshow(_type, np.kron(img, np.ones((self.magnify, self.magnify))))
        cv2.waitKey(1)


if __name__ == "__main__":
    import numpy as np
    pix = np.random.rand(200,200) 
    while True:
        dp = (np.random.rand(200, 200) - 0.5 ) / 2.0
        pix = pix + dp
        cv2.imshow('image', pix)
        cv2.waitKey(1)
