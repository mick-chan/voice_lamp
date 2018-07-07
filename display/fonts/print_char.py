from font_atari_4x8 import FontAtariSmall

f = FontAtariSmall()
f.setCharacter("A")
for y in range(f.getHeight()):
    line = "|"
    for x in range(f.getWidth()):
        if f.getPixel(x, y) != 0:
            line += "#"
        else:
            line += " "
    line += "|"
    print line
