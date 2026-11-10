# MGT 4250 Fall 2026 - Class 18

This repository contains a small Python data visualization project built with Streamlit. It loads a sample Superstore dataset from Excel and creates an interactive dashboard to explore sales and profitability across states, categories, and time periods.

## Project overview

The app demonstrates how to:

- load an Excel workbook with pandas
- filter and transform a retail dataset
- build dashboard-style visualizations with Plotly
- present the results in a Streamlit web interface

The dashboard focuses on a subset of states and displays:

- profit margin by state
- profit margin by product category
- category trends over time
- sales composition by sub-category

## Repository contents

- `class17.py` – main Streamlit app and visualization logic
- `sample_-_superstore.xls` – sample dataset used in the app
- `requirements.txt` – Python package dependencies
- `README.md` – project documentation

## Tech stack

- Python
- pandas
- Streamlit
- Plotly
- matplotlib
- openpyxl
- xlrd

## Installation

Clone the repository and create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the app

From the repository root:

```bash
streamlit run class17.py
```

The app expects the Excel file `sample_-_superstore.xls` to be in the same directory as `class17.py`.

## Data description

The application reads the sample Superstore dataset and uses fields such as:

- `State/Province`
- `Country/Region`
- `Category`
- `Sub-Category`
- `Order Date`
- `Sales`
- `Profit`
- `Quantity`

These fields power the dashboards and summaries shown in the Streamlit interface.

## Notes

This project is a classroom-style example and is intentionally lightweight. It is not organized as a full production application, but it is a useful reference for exploring how pandas and Plotly can be combined to create an interactive dashboard in Python.
