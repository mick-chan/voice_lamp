#
# Font interface
#

class Font:
    def __init__(self):
        self.mChar = "A"

    def setCharacter(self, ch):
        self.mChar = ch

    def getWidth(self):
        return 0

    def getHeight(self):
        return 0

    def getPixel(self, x, y):
        return 0


