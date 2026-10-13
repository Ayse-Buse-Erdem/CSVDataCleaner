# CSV Data Cleaner and Analyzer

A Python application that cleans and analyzes product data stored in CSV format.

## Features

- Reads and validates CSV files
- Detects missing values
- Detects and removes duplicate records
- Fills missing numerical and text values
- Calculates basic statistics
- Creates category-based summaries
- Exports cleaned data and analysis reports

## Technologies

- Python
- pandas

## Installation

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```powershell
pip install -r requirements.txt
```

## Usage

Run the application:

```powershell
python main.py
```

## Tests

Run the automated tests:

```powershell
python -m unittest test_data_cleaner.py -v
```