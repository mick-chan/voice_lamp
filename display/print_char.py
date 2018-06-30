import font_atari_4x8 as f

ch = f.font_bitmap["e"]
for y in range(len(ch)):
    line = "|"
    for x in range(4):
        if (ch[y] & (1 << (7 - x))) != 0:
            line += "#"
        else:
            line += " "
    line += "|"
    print line
