
class Layer:
    """
    Decorator pattern abstract component interface to encapsulate
    a display filter to be applied on top of a stack of layers to
    modify the displayed image.  
    """

    def __init__(self, layer):
        self.mLayer = layer

    def process(self):
        raise Exception("Abstract class")       

    def apply(self):
	raise Exception("Abstract class")

    def getWidth(self):
        raise Exception("Abstract class")

    def getHeight(self):
        raise Exception("Abstract class")

    def getPixel(self, x, y):
	raise Exception("Abstract class")

    def setPixel(self, x, y):
	raise Exception("Abstract class")

def main():
    layer = Layer(None)
    try:
        layer.apply()
    except Exception:
        print "Test passed"

if __name__ == "__main__":
    # execute only if run as a script
    main()
