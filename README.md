# Sudoku Puzzle Generator

A simple Python-based Sudoku puzzle generator.

## Introduction

This project provides a straightforward implementation of a Sudoku puzzle generator. It first produces a full valid Sudoku grid, then randomly removes numbers to create puzzles. This tool can be helpful for Sudoku enthusiasts or developers looking for a basic generator to integrate into their applications.

## Features

- Generates full valid Sudoku grids.
- Random removal of numbers to create puzzles.
- Customizable difficulty by adjusting the number of removed numbers.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sonnymay/sudoku-generator.git
   cd sudoku-generator
   ```

2. There are no external dependencies. Just ensure you have Python 3.x installed.

## Usage

Run the main script:

```bash
python sudoku_generator.py
```

This will display a full Sudoku grid, followed by a generated puzzle.

## Customizing Difficulty

To adjust the difficulty of the generated puzzle, modify the `num_holes` parameter in the `generate_puzzle` function. More holes typically lead to a harder puzzle, but ensure the puzzle remains solvable.

```python
generator.generate_puzzle(num_holes=50)  # Adjust the number as desired
```

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## License

This project is open-sourced and licensed under the MIT License.

## Acknowledgments

Special thanks to:

- OpenAI's Assistant for guidance and code snippets.
- All Sudoku enthusiasts and contributors to the project.

## Connect

GitHub: [@sonnymay](https://github.com/sonnymay)

---
