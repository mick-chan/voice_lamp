import sys
sys.path.insert(0, "fonts")
import time
from Display import Display
from InvertLayer import InvertLayer
from FontLayer import FontLayer

def main():
    display = Display()
    fontLayer = FontLayer(display, "atari", "i")
    invertLayer = InvertLayer(fontLayer)
    invertLayer.process()
    invertLayer.apply()
    time.sleep(2)

if __name__ == "__main__":
    # execute only if run as a script
    main()

