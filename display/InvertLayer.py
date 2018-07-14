import sys
from Layer import Layer
from Display import Display

class InvertLayer(Layer):
    """
    Decorator class that inverts all pixel values.
    """

    def __init__(self, layer):
        self.mLayer = layer

    def process(self):
        for y in range(self.getHeight()):
            for x in range(self.getWidth()):
                p = self.mLayer.getPixel(x, y)
                self.mLayer.setPixel(x, y, (255 - p[0], 255 - p[1], 255 - p[2]))

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
    display = Display()
    invertLayer = InvertLayer(display)
    invertLayer.process()    
    for y in range(invertLayer.getHeight()):
        for x in range(invertLayer.getWidth()):
            if invertLayer.getPixel(x, y) != (255, 255, 255):
                print "Test failed"
                return
    print "Test passed"

if __name__ == "__main__":
    # execute only if run as a script
    main()
