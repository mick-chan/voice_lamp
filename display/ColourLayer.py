import sys
from Layer import Layer
from FontLayer import FontLayer
from Display import Display

class ColourLayer(Layer):
    """
    Decorator class that applies colour to foreground and
    background pixels. Foreground pixels are any non-zero
    value pixels.
    """

    def __init__(self, layer, foreground, background):
        Layer.__init__(self, layer)
        assert(len(foreground) == 3)
        assert(len(background) == 3)
        self.mForeground = foreground
        self.mBackground = background

    def process(self):
        self.mLayer.process()
        for y in range(self.getHeight()):
            for x in range(self.getWidth()):
                if self.mLayer.getPixel(x, y) == (0, 0, 0):
                    self.mLayer.setPixel(x, y, self.mBackground)
                else:
                    self.mLayer.setPixel(x, y, self.mForeground)

    def apply(self):
        self.mLayer.apply()

    def getWidth(self):
        return self.mLayer.getWidth()

    def getHeight(self):
        return self.mLayer.getHeight()

    def getPixel(self, x, y):
        return self.mLayer.getPixel(x, y)

    def setPixel(self, x, y, pixel):
        self.mLayer.setPixel(x, y, pixel)


def main():
    import time
    display = Display()
    fontLayer = FontLayer(display, "atari", "A")
    colourLayer = ColourLayer(fontLayer, (255, 0, 0), (0, 255, 0))
    colourLayer.process()
    colourLayer.apply()
    for y in range(colourLayer.getHeight()):
        for x in range(colourLayer.getWidth()):
            if colourLayer.getPixel(x, y) != (255, 0, 0) and \
               colourLayer.getPixel(x, y) != (0, 255, 0):
                print "Test failed"
                return
    print "Test passed"
    time.sleep(3)

if __name__ == "__main__":
    # execute only if run as a script
    main()
