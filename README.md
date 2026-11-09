# edu-pixel-art

Render pixel art from a text file:

```sh
python3 main.py data/test.txt
```

Print the complete xterm-256 color palette with its indexes. The RGB cube is
shown in one table, with red levels as columns:

```sh
python3 main.py --palette
```

The file has a `[colours]` section that maps names to xterm-256 palette indexes
(0-255), separated by whitespace, followed by a `[diagram]` section. Each
diagram row contains space-separated chunks, with each chunk written as a pixel
count followed by a color name. The terminal formatting is reset to its default
after each output row. The renderer uses half blocks to pack each pair of input
rows into one terminal row, roughly halving the image height while preserving
the vertical pixel detail.

```text
[colours]
Bl 4
W 7

[diagram]
12Bl 6W
```
