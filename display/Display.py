import sys
from Layer import Layer
import unicornhat as uh

class Display(Layer):
    """
    Root Decorator class that stores image state and writes
    image onto the Unicorn pHAT.
    """

    def __init__(self):
        Layer.__init__(self, None)
        uh.set_layout(uh.PHAT)
        self.mWidth = 4
        self.mHeight = 8
        # mValues is a mWidth x mHeight array of tuples formatted
        # as (r, g, b) values for that pixel.
        self.mValues = [[(0, 0, 0) for x in range(self.mWidth)] for y in range(self.mHeight)]

    def process(self):
        # No processing to do, we only want to display our state.
        pass

    def apply(self):
        # The display coordinates (xp, yp) mapping to image pixels (x, y)
        # x = mWidth - 1 - yp
        # y = xp
        uh.clear()
        for xp in range(self.mHeight):
            y = xp
            for yp in range(self.mWidth):
                x = self.mWidth - 1 - yp
                p = self.getPixel(x, y)
                uh.set_pixel(xp, yp, p[0], p[1], p[2])
        uh.show()

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def getPixel(self, x, y):
        assert(x >= 0 and x < self.mWidth)
        assert(y >= 0 and y < self.mHeight)
        p = self.mValues[y][x]
        return p

    def setPixel(self, x, y, pixel):
        assert(len(pixel) == 3)
        self.mValues[y][x] = pixel


def main():
    display = Display()
    p0 = display.getPixel(3, 4)
    if p0[0] != 0 or p0[1] != 0 or p0[2] != 0:
        print "Test failed"
    else:
        print "Test passed"

    p1 = (128, 144, 188)
    display.setPixel(3, 4, p1)
    p2 = display.getPixel(3, 4)
    if p2[0] != p1[0] or p2[1] != p1[1] or p2[2] != p1[2]:
        print "Test failed"
    else:
        print "Test passed"

if __name__ == "__main__":
    # execute only if run as a script
    main()
