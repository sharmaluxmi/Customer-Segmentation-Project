import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_excel("../Dataset/Flipkart_Clean_Dataset.xlsx")

print("\n===== DATASET OVERVIEW =====")
print(df.head())

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== SUMMARY STATISTICS =====")
print(df.describe())

# Basic KPIs
total_revenue = df["Revenue"].sum()
total_customers = df["Customer_ID"].nunique()
total_orders = len(df)

print(f"Total Revenue: {total_revenue:,.2f}")
print(f"Total Customers: {total_customers}")
print(f"Total Orders: {total_orders}")

# Revenue by Category
if "Category" in df.columns:
    revenue_by_category = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
    print("\nRevenue by Category")
    print(revenue_by_category)
