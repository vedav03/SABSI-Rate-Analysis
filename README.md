# SABSI Rate Analysis (Australia, 2010–2023)

This project analyzes time-series data on Staphylococcus Aureus Bloodstream Infections (SABSI) in Australian hospitals using Python. 
The goal is to identify infection trends over time, quantify yearly changes, and visualize the impact of events like COVID-19.

## 📁 Dataset

- Source: MyHospitals SABSI Summary Tables 2023–24 (Excel)
- Table Used: Table 2 – Time-series data
- Metric: SABSI rates per 10,000 patient-days

## 🔧 Tools Used

- Python (pandas, matplotlib, numpy, scipy)
- Excel file processing and data cleaning
- Linear regression (`scipy.stats.linregress`)
- Data visualization (`matplotlib`)

## 📊 Key Steps

- Cleaned and parsed Excel sheet
- Extracted SABSI rates from 2010–2023
- Computed trend line and slope
- Calculated mean, median, std dev, and yearly change
- Plotted trend with COVID-19 period highlighted

## 📈 Output

- Identified trend direction via regression
- Visualized rates over time with annotations
- Highlighted peak rate and COVID-19 window

> See `sabsi_analysis.py` for full code and visual output.
