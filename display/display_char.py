import sys
import time
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
    f = createFont(sys.argv[1])
    f.setCharacter(sys.argv[2][0])
    # x = 3 - yp
    # y = xp
    uh.set_layout(uh.PHAT)
    for xp in range(8):
        y = xp
        for yp in range(4):
            x = 3 - yp
            if f.getPixel(x, y) != 0:
                uh.set_pixel(xp, yp, 30, 50, 150)
    uh.show()
    time.sleep(5)

if __name__ == "__main__":
    # execute only if run as a script
    main()
