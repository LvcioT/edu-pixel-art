# Contributing to edu-pixel-art

Thanks for your interest in improving this project.

This project is meant to be a simple educational tool for teachers and students. Contributions are especially welcome if they help make the project easier to use, more engaging for learners, or richer in sample templates.

## Ways to contribute

- Add new pixel-art templates in the `data/` folder
- Improve the README or project documentation
- Fix bugs or make the renderer easier to understand
- Suggest better examples for classroom use
- Help make the project more beginner-friendly

## Template format

Templates live in the `data/` directory as plain text files. Each file should contain:

- a `[colours]` section with color names and xterm palette indexes
- a `[diagram]` section with run-length encoded pixel rows

Example:

```text
[colours]
W 231
B 16
G 2

[diagram]
12W 6B
15W
```

For a more detailed example, see the existing files in `data/`.

## Making a change

1. Fork the repository or create a new branch.
2. Make your change in a focused, easy-to-read way.
3. Test the project with the relevant command.
4. Submit a pull request with a short explanation of what you changed.

## Running the project

Render a template:

```bash
python3 main.py data/test.txt
```

Print the palette:

```bash
python3 main.py --palette
```

## Community expectations

Please keep contributions respectful, clear, and beginner-friendly. Educational projects work best when examples are easy to follow and welcoming to newcomers.
