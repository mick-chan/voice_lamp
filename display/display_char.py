import sys
import time
import colorsys
sys.path.insert(0, "fonts")
from font_atari_4x8 import FontAtariSmall
from font_quarky_dot_matrix import FontQuarkyDotMatrix
import unicornhat as uh

def createFont(fontName):
    print "Create font:", fontName
    if fontName == "atari":
        print "Created atari font"
        return FontAtariSmall()
    elif fontName == "quarky":
        print "Created quarky font"
        return FontQuarkyDotMatrix()
    else:
        return None

def main():
    print "Starting"
    if len(sys.argv) != 3:
        print sys.argv
        print "Usage: %s <font name> <character>" % (sys.argv[0])
        return
    uh.set_layout(uh.PHAT)
    f = createFont(sys.argv[1])
    if sys.argv[2] == "all":
        displayLowercaseAlphabet(f)
        displayUppercaseAlphabet(f)
        displayNumbers(f)
    elif sys.argv[2] == "numbers":
        displayNumbers(f)
    elif sys.argv[2] == "uppercase":
        displayUppercaseAlphabet(f)
    elif sys.argv[2] == "lowercase":
        displayLowercaseAlphabet(f)
    else:
        f.setCharacter(sys.argv[2])
        displayCharacter(f)
        time.sleep(5)

def displayLowercaseAlphabet(f):
    for ch in range(ord('a'), ord('z') + 1):
        f.setCharacter(chr(ch))
        displayCharacter(f)
        time.sleep(2)

def displayUppercaseAlphabet(f):
    for ch in range(ord('A'), ord('Z') + 1):
        f.setCharacter(chr(ch))
        displayCharacter(f)
        time.sleep(2)

def displayNumbers(f):
    for ch in range(ord('0'), ord('9') + 1):
        f.setCharacter(chr(ch))
        displayCharacter(f)
        time.sleep(2)

def displayCharacter(f):
    # x = 3 - yp
    # y = xp
    hue = int(time.time() * 10) % 360
    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue / 360.0, 1.0, 1.0)]
    uh.clear()
    for xp in range(8):
        y = xp
        for yp in range(4):
            x = 3 - yp
            if f.getPixel(x, y) != 0:
                uh.set_pixel(xp, yp, r, g, b)
    uh.show()

if __name__ == "__main__":
    # execute only if run as a script
    main()
