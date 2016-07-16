# Image patch generate
import math
import numpy as np
import matplotlib as mpl


class GetAngle(object):
    """Generate a random angle between 0 to pi/2"""

    # def __init__(self, data):
    # self.data=data
    @staticmethod
    def get_angle():
        angle = math.pi / 2 * np.random.random((1,))
        return float(angle)
        pass

    def function(self):
        pass

    @staticmethod
    def gaussian_2d(shape=(3, 3), sigma=0.5):
        """
        2D gaussian mask - should give the same result as MATLAB's
        fspecial('gaussian',[shape],[sigma])
        """

        m, n = [(ss-1.)/2. for ss in shape]
        y, x = np.ogrid[-m:m+1, -n:n+1]
        h = np.exp(-(x*x + y*y) / (2.*sigma*sigma))
        h[h < np.finfo(h.dtype).eps*h.max()] = 0
        sumh = h.sum()
        if sumh != 0:
            h /= sumh
        return h

