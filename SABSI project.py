# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
file_path = "C:/Users/vedav/Downloads/MyHospitals-SABSI-summary-tables-2023-24.xlsx"

# Viewing available sheets within the Excel file downloaded from the Australian Government's health statistics website.
sheet_name = pd.ExcelFile(file_path).sheet_names
print("Available Sheets:", sheet_name)

# Loading Table - 2 (Time - Series Data)
table2 = pd.read_excel(file_path, sheet_name="Table 2", header=1)

# Cleaning the sheet. Many values were either missing or jumbled with variable names instead of values.
table2 = table2.dropna(how="all", axis=1)  
table2 = table2.dropna(subset=[table2.columns[0]], how="all")   
table2 = table2.rename(columns={table2.columns[0]: "Metric:"})
table2.columns = [col.split("–")[0] if "–" in str(col) else col for col in table2.columns]
table2 = table2.replace("n.p.", pd.NA)  # Replace "n.p." with NaN

# Examining SABSI trends over time.
target_idx = table2.index[table2["Metric:"] == "All SABSI cases"][0]

# Get the RATES which are 2 rows below the "All SABSI cases"), skipping the "Metrics" column. 
rates_row = table2.iloc[target_idx + 2, 1:]   

# Converting to numeric values to perform Regression and then later, the graphical depiction of my analysis.
rates = pd.to_numeric(rates_row, errors='coerce')  

# Extracting years from column names (excluding "Metric:")
years = [int(col.split()[-1]) for col in table2.columns[1:]]  

# Calculating the Regression of the Rates over time to ascertain whether the 
# trends are escalating or not as time goes on. 
from scipy.stats import linregress
slope, intercept, r_value, p_value, std_error = linregress(years, rates)
trend_line = slope * np.array(years) + intercept
print("The slope is:", slope)

# Adding Summary Statistics to derieve further insights, providing a numerical
# snapshot to complement the trend line.
mean_rate = rates.mean()
median_rate = rates.median()
std_rate = rates.std()
yearly_change = rates.diff().mean()
print(f"Mean SABSI Rate: {mean_rate:.2f} cases per 10,000 patient-days")
print(f"Median SABSI Rate: {median_rate:.2f} cases per 10,000 patient-days")
print(f"Standard Deviation: {std_rate:.2f}")
print(f"Average Yearly Change: {yearly_change:.2f}") 

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(years, rates, marker='o', linestyle='-', linewidth=2, label="SABSI Rates")
plt.plot(years, trend_line, linestyle='--', color='green', label=f"Trend (slope={slope:.4f})")
plt.xticks(years, rotation=45)
plt.title("Australian Hospital SABSI Rates (2010–2023) with Trend", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Cases per 10,000 patient-days", fontsize=12)
plt.axvspan(2020, 2022, color='red', alpha=0.1, label="COVID-19 Period")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Annotating the peak value
max_rate_year = years[rates.argmax()]
max_rate = rates.max()
plt.annotate(f"Peak: {max_rate:.2f}", xy=(max_rate_year, max_rate), 
             xytext=(max_rate_year + 1, max_rate + 0.1),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()
 
