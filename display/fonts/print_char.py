import sys
from font_atari_4x8 import FontAtariSmall
from font_quarky_dot_matrix import FontQuarkyDotMatrix
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
        print "Usage: %s <font name> <character>" % (sys.argv[0])
        return
    f = createFont(sys.argv[1])
    f.setCharacter(sys.argv[2])
    for y in range(f.getHeight()):
        line = "|"
        for x in range(f.getWidth()):
            if f.getPixel(x, y) != 0:
                line += "##"
            else:
                line += "  "
        line += "|"
        print line

if __name__ == "__main__":
    # execute only if run as a script
    main()
