import cv2

class Drawer():

    cv2.namedWindow("strats")
    cv2.namedWindow("reputations")
    cv2.namedWindow("totals")

    def draw(self, img, _type="strats"):
        cv2.imshow(_type, img)
        cv2.waitKey(1)

if __name__ == "__main__":
    import numpy as np
    pix = np.random.rand(200,200) 
    while True:
        dp = (np.random.rand(200, 200) - 0.5 ) / 2.0
        pix = pix + dp
        cv2.imshow('image', pix)
        cv2.waitKey(1)
