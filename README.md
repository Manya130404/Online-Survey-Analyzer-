# Online-Survey-Analyzer-
# Online Survey Data Analyzer

## Overview

This project implements an end-to-end data pipeline to analyze survey data.
It reads data from a CSV file, processes it, performs analysis, generates visualizations, and stores the processed output.

---

## Features

* Data ingestion from CSV
* Data cleaning and preprocessing
* Statistical analysis
* Data visualization
* Storage of processed data

---

## Project Structure

```
survey-analyzer/
│── app.py
│── data/
│   └── survey.csv
│── output/
│   ├── gender_distribution.png
│   ├── platform_usage.png
│   ├── age_distribution.png
│   └── processed_data.csv
│── src/
│   ├── ingestion.py
│   ├── processing.py
│   ├── analysis.py
│   ├── visualization.py
│   └── storage.py
│── README.md
```

---

## Technologies Used

* Python
* Pandas
* Matplotlib

---

## How to Run

1. Install dependencies:

```
pip install pandas matplotlib
```

2. Run the project:

```
python app.py
```

---

## Output

* Graphs:

  * Gender distribution (bar chart)
  * Platform usage (pie chart)
  * Age distribution (histogram)

* Processed dataset:

```
output/processed_data.csv
```

---

## Future Improvements

* Real-time data integration
* Database integration
* Web-based dashboard
* Advanced analytics

---

## Author

Name: Your Name
Roll Number: Your Roll Number
Course: Your Course Name
