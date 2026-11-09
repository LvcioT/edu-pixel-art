# edu-pixel-art

Render pixel art from a text file:

```sh
python3 main.py data/test.txt
```

The file has a `[colours]` section that maps names to standard ANSI foreground
color codes (30-37 or 90-97), separated by whitespace, followed by a
`[diagram]` section. Each diagram row contains space-separated chunks, with each
chunk written as a pixel count followed by a color name. The terminal
formatting is reset to its default after each output row. The renderer uses half
blocks to pack each pair of input rows into one terminal row, roughly halving
the image height while preserving the vertical pixel detail.

```text
[colours]
Bl 34
W 37

[diagram]
12Bl 6W
```
