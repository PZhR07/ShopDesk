# Advance Python

A lightweight desktop app for managing a small shop, its products, customers, and invoices. Built with Python, Tkinter, and SQLite, it runs locally without a separate database server.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-2C5F2D)](https://docs.python.org/3/library/tkinter.html)
[![Database](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)

## Features

- **Contact management** — add, search, update, display, and delete customer contacts.
- **Product management** — maintain product names, prices, and stock quantities.
- **Invoice management** — create and search customer invoices, including date-based searches.
- **Shop workflow** — select products and quantities, process purchases, and create invoices for registered customers.
- **Local storage** — records are stored in an SQLite database; CSV export/backup actions are available in the app.
- **Input checks** — basic validation for names, phone numbers, quantities, prices, and dates.

## Requirements

- Python 3.10 or newer
- Tkinter (included with most Python installers; on Debian/Ubuntu, install it with `sudo apt install python3-tk`)
- `persiantools` (used for date conversion)

## Getting started

1. Clone the repository and open its folder:

   ```bash
   git clone <repository-url>
   cd Advance_Python
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   macOS / Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install the Python dependency:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   python main.py
   ```

   On Windows, you can use `py main.py` if the `python` command is unavailable.

The first window lets you choose **Shop** or **Database**. Choose **Database** to open the contact, product, or invoice manager.

## Data and backups

The app reads and writes `database.db` in its current working directory. The database and generated CSV backups are ignored by Git, so your local records are not included when you push this project. Keep your own backups if you need to preserve your data.

Some backup actions currently copy files to a developer-specific Windows folder under `C:\Users\Parsa\Desktop\Advance_Python\backups`. On another computer, those actions may need their destination path updated. The database file itself remains in the project’s current working directory.

## Project structure

| File | Purpose |
| --- | --- |
| `main.py` | Starts the app and provides the Shop / Database selector. |
| `GUI.py` | Tkinter screens for contacts, products, and invoices. |
| `Shop.py` | Product browsing and purchase workflow. |
| `Database.py` | SQLite operations and CSV/database backup actions. |
| `Security.py` | Input validation and SQLite helper functions. |
| `requirements.txt` | Python package dependencies. |

## Notes

- This is a local desktop application; it does not require an online account or hosted database.
- The interface labels are currently in English.

## License

No license file is currently included. Add a `LICENSE` file before publishing if you want to specify how others may use, modify, or distribute this project.
