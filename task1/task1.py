# task1.py
import pandas as pd

# Load the Excel dataset
file_path = "Delinquency_prediction_dataset.xlsx"

try:
    df = pd.read_excel(file_path)
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error reading Excel file: {e}")
    exit()

# Basic overview
print(f"Columns: {df.columns}")
print(f"Number of rows: {len(df)}\n")
print("First 5 rows:")
print(df.head())

# Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Step 2: Handle missing data for key numeric columns
numeric_cols = ["Income", "Credit_Score", "Loan_Balance"]
for col in numeric_cols:
    median_val = df[col].median()
    df[col] = df[col].fillna(median_val)  # Avoid inplace warning
    print(f"Filled missing values in '{col}' with median: {median_val}")

# Step 3: Detect high-risk customers
# Define high-risk based on Credit_Utilization > 0.5 and Missed_Payments >= 3
high_utilization = df[df["Credit_Utilization"] > 0.5]
high_missed_payments = df[df["Missed_Payments"] >= 3]

print("\nHigh-risk customers:")
print(f"Customers with >50% credit utilization: {len(high_utilization)}")
print(f"Customers with >=3 missed payments: {len(high_missed_payments)}")

# Step 4: Save cleaned dataset
cleaned_file = "Delinquency_dataset_cleaned.xlsx"
df.to_excel(cleaned_file, index=False)
print(f"\nCleaned dataset saved as '{cleaned_file}'")
