# 🚀 Data Profiler

A Streamlit-based data profiling and analysis application designed to help users quickly understand, inspect, clean, analyze, and visualize their datasets.

## 📌 Project Overview

Data Profiler provides an interactive interface for exploring datasets without requiring extensive manual analysis.

Users can upload a dataset and perform different data analysis tasks through a simple Streamlit interface.

The application focuses on:

- Dataset overview
- Data summary
- Data cleaning
- Statistical analysis
- Data visualization
- Automated reporting
- Data quality inspection

## ✨ Features

### 📂 Dataset Upload
- Upload CSV and Excel datasets
- Automatically load the uploaded dataset
- Display basic dataset information

### 📊 Dataset Overview
- Number of rows and columns
- Column names
- Data types
- Missing values
- Unique values
- Dataset structure

### 📋 Summary
- Descriptive information
- Column-wise summaries
- Numerical and categorical data insights

### 🧹 Data Cleaning
- Missing value analysis
- Duplicate row detection
- Data type inspection
- Basic data cleaning operations

### 📈 Statistics
- Descriptive statistics
- Numerical analysis
- Statistical summaries
- Distribution-related insights

### 📊 Visualization
- Graphical representation of data
- Numerical and categorical visualizations
- Interactive data exploration

### 📄 Report
- Generate a consolidated data profiling report
- Present important dataset quality information in an organized format

### ℹ️ About
- Project information
- Technologies used
- Project purpose
- Future improvements

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- OpenPyXL
- Pillow

## 📁 Project Structure

```text
Data-Profiler/
│
├── app.py
├── requirements.txt
├── README.md
│
└── modules/
    ├── home.py
    ├── workspace.py
    ├── dataset_overview.py
    ├── summary.py
    ├── cleaning.py
    ├── statistics.py
    ├── visualization.py
    ├── report.py
    └── about.py