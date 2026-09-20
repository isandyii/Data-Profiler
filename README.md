# 🚀 Data Profiler

A Streamlit-based data profiling and analysis application designed to help users quickly understand, inspect, clean, edit, analyze, and visualize their datasets.

## 📌 Project Overview

Data Profiler provides an interactive interface for exploring and preparing datasets without requiring extensive manual analysis.

Users can upload CSV or Excel datasets and perform different data analysis and cleaning tasks through an interactive Streamlit workspace.

The application focuses on:

- Dataset overview
- Data summary
- Data cleaning
- Specific value editing
- Statistical analysis
- Data visualization
- Automated reporting
- Data quality inspection

## ✨ Features

### 📂 Dataset Upload

- Upload CSV and Excel datasets
- Automatically load the uploaded dataset
- Display basic dataset information
- Support multiple dataset formats through a unified workspace

### 📊 Dataset Overview

- Number of rows and columns
- Column names
- Data types
- Missing values
- Unique values
- Duplicate row detection
- Duplicate column detection
- Dataset structure

### 📋 Summary

- Descriptive information
- Column-wise summaries
- Numerical and categorical data insights
- Missing-value analysis
- Data quality information

### 🧹 Data Cleaning

- Missing value analysis
- Handle missing values using suitable aggregation methods
- Mean and median based value replacement
- Duplicate row detection and removal
- Duplicate column detection and removal
- Column renaming
- Data type conversion
- Basic data cleaning operations

### ✏️ Specific Value Editing

- Edit individual dataset values directly
- Interactive data editor
- Apply changes without modifying the entire dataset
- Review and update specific cells when required

### 📈 Statistics

- Descriptive statistics
- Numerical analysis
- Statistical summaries
- Distribution-related insights
- Dataset-level statistical information

### 📊 Visualization

- Graphical representation of data
- Numerical visualizations
- Categorical visualizations
- Distribution plots
- Matplotlib-based visualizations
- Seaborn-based statistical visualizations
- Interactive data exploration

### 📄 Report

- Generate a consolidated data profiling report
- Present important dataset quality information
- Summarize key dataset characteristics
- Organize profiling results into a structured report

### ℹ️ About

- Project information
- Technologies used
- Project purpose
- Application capabilities
- Future improvements

## 🆕 What's New

The latest update introduces several improvements to the Data Profiler.

### 📂 CSV + Excel Support

The application now supports both CSV and Excel datasets, allowing users to work with different commonly used data formats.

### 🧹 Aggregation-Based Missing Value Handling

Missing values can now be handled using suitable aggregation methods such as mean and median, depending on the dataset and column.

### ✏️ Specific Value Editing

Users can now directly edit individual cells in their dataset using an interactive data editor.

### 📈 Seaborn Integration

Seaborn has been added to provide additional statistical and data visualization capabilities.

### ✨ Redesigned User Interface

The application now includes a redesigned interactive interface with improved layout, visual elements, and user experience.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
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
├── assets/
│   ├── image1.png
│   ├── demo_file.csv
│   └── demo_file.xlsx
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