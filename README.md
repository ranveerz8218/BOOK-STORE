# Books Manager

A simple command-line application built with Python to manage a personal book collection. Add, search, view, and delete books, with all data automatically saved to a text file so your list persists between runs.

## Features

- **Add a Book** — Store a book's name, author, and page count.
- **Lookup a Book** — Search by keyword in the book's title or author name (case-insensitive).
- **Display Books** — View your entire book collection at a glance.
- **Delete a Book** — Remove a book from your collection by name.
- **Persistent Storage** — Your book list is automatically loaded from and saved to `TheBooksList.txt`.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/books-manager.git
   cd books-manager
   ```
2. Make sure `main.py` and `TheBooksList.txt` are in the same directory. If `TheBooksList.txt` doesn't exist yet, the program will automatically create one for you when you save.

### Usage

Run the program with:

```bash
python main.py
```

You'll be presented with a menu:

```
*** Books Manager ***
1) Add a Book
2) Lookup a Book
3) Display Books
4) Delete a Book
5) Quit
```

Enter the number corresponding to the action you want to perform, and follow the on-screen prompts.

## Data Format

Books are stored in `TheBooksList.txt` as comma-separated values, one book per line:

```
Book Name,Author Name,Page Count
```

Example:

```
IT,S KING,500
HARRY POTTER,JK ROWLING ,400
NEW LIFE,GEORGE,350
```

## How It Works

- On startup, the program reads `TheBooksList.txt` and loads existing books into memory. If the file doesn't exist, it starts with an empty list.
- Changes made during the session (adding/deleting books) are kept in memory.
- When you choose to quit (option 5), the current book list is written back to `TheBooksList.txt`, overwriting the previous contents.

## Notes / Possible Improvements

- Book titles are currently required to match exactly (case-insensitive) when deleting — partial matches aren't supported.
- No validation is currently performed on the page count field (it's stored as a string).
- Duplicate book entries are allowed.

## License

No License Specified yet.