# Text & Word Frequency Analyzer (CLI)

A command-line tool that analyzes any text file, removes punctuation, filters alphabetical words, and generates a frequency ranking of the most commonly used words.

## Features

- Computes total words and count of unique words.
- Displays Top 10 most frequent words in a formatted table.
- Optional report export to file (or default `record.json`).
- Includes a sample test file (`sample.txt`).

## How to Run

```bash
python word_frequency_analyzer/main.py
```
When prompted for a file path, you can enter `word_frequency_analyzer/sample.txt` to test it immediately.
*(No external dependencies required — runs using Python's standard library.)*
