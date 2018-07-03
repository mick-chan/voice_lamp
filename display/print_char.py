import font_atari_4x8 as f

ch = f.font_bitmap["E"]

for x in range(len(ch)):
    line = "|"
    for y in range(8):
        if (ch[x] & (1 << (7 - y))) != 0:
            line += "#"
        else:
            line += " "
    line += "|"
    print line
