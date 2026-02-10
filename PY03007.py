#XỬ LÝ VĂN BẢN
import sys
content = sys.stdin.read()

lines = content.translate(str.maketrans(".!?", "\n\n\n")).split("\n")

for line in lines:
    if any(char.isalnum() for char in line):
        print(' '.join(line.split()).lower().capitalize() )
