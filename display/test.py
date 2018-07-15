import sys
sys.path.insert(0, "fonts")
import time
from Display import Display
from ColourLayer import ColourLayer
from InvertLayer import InvertLayer
from FontLayer import FontLayer

def main():
    display = Display()
    fontLayer = FontLayer(display, "atari", "i")
    colourLayer = ColourLayer(fontLayer, (255, 0, 0), (0, 255, 0))
    invertLayer = InvertLayer(colourLayer)
    invertLayer.process()
    invertLayer.apply()
    time.sleep(2)

if __name__ == "__main__":
    # execute only if run as a script
    main()

