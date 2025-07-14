# Trie Autocomplete Implementation

This project demonstrates how to implement an autocomplete feature using a Trie data structure. The goal is to suggest and rank words based on the prefixes entered by the user.

## Project Overview

Autocomplete is a feature widely used in various applications such as search engines, text editors, and messaging apps. The project uses a **Trie** (prefix tree) to efficiently store and search for words based on the user's input. The Trie structure allows for fast prefix matching and word ranking based on frequency.

## Features

- **Word Storage**: The program reads multiple text files containing words and stores them in a Trie.
- **Prefix Autocomplete**: As the user types a prefix, the program suggests words that start with that prefix, ranked by frequency.
- **File Input**: Users can input the name of a file, which contains other files with words (e.g., dictionary.txt, novel.txt).
- **Frequency Tracking**: Each word's frequency is tracked, and words are suggested in descending order of frequency.
- **File Validation**: The program throws exceptions if files do not exist.

## File Input Format

- The user is prompted to enter a file name (e.g., `abc.txt`).
- The file contains a list of text files, each containing a list of words. These words will be inserted into the Trie.

## How to Use

1. **Run the Program**:
   Execute the program, and it will prompt you to input a file name (e.g., `abc.txt`).
   
2. **File Loading**:
   The program loads all words from the files listed inside the input file. It supports multiple files, each containing words to be inserted into the Trie.

3. **Autocomplete**:
   After the file is loaded, you can type a prefix (e.g., "ca") to get a ranked list of words starting with that prefix. The words are ranked based on their frequency of appearance.

4. **Quit**:
   To exit the program, enter `0` when prompted for a prefix.
