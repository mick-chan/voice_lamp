import sys
sys.path.insert(0, "fonts")
from font_atari_4x8 import FontAtariSmall
from font_quarky_dot_matrix import FontQuarkyDotMatrix
from Layer import Layer
from Display import Display

class FontLayer(Layer):
    """
    Decorator class that overlays a font character onto the display.
    """

    def __init__(self, layer, fontName, ch):
        self.mLayer = layer
        if fontName == "atari":
            self.mFont = FontAtariSmall()
        elif fontName == "quarky":
            self.mFont = FontQuarkyDotMatrix()
        else:
            raise Exeption("Cannot instantiate font %s" % fontName)
        print "Created %s font" % fontName
        self.mFont.setCharacter(ch)

    def process(self):
        assert(self.mLayer.mWidth == self.mFont.getWidth())
        assert(self.mLayer.mHeight == self.mFont.getHeight())
        for y in range(self.mLayer.mHeight):
            for x in range(self.mLayer.mWidth):
                if self.mFont.getPixel(x, y) != 0:
                    self.mLayer.setPixel(x, y, (255, 255, 255))

    def apply(self):
        self.mLayer.apply()

    def getPixel(self, x, y):
        return self.mLayer.getPixel(x, y)

    def setPixel(self, x, y, pixel):
        self.mLayer.setPixel(x, y, pixel)


def main():
    display = Display()
    f = FontAtariSmall()
    f.setCharacter("i")
    fontLayer = FontLayer(display, "atari", "i")
    fontLayer.process()
    for y in range(f.getHeight()):
        for x in range(f.getWidth()):
            if f.getPixel(x, y) != 0:
                if fontLayer.getPixel(x, y)[0] == 0:
                    print "Test failed"
                    return
    print "Test passed"

if __name__ == "__main__":
    # execute only if run as a script
    main()
