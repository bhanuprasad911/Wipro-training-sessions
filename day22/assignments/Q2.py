import pandas as pd
import numpy as np
#Load CSV into DataFrame
df = pd.read_csv("sales.csv")
print("Original Data:")
print(df)
#Add new column "Total"
df["Total"] = df["Quantity"] * df["Price"]
print("\nData with Total column:")
print(df)
#NumPy Calculations
total_sales = np.sum(df["Total"])
average_sales = np.mean(df["Total"])
std_sales = np.std(df["Total"])

print("Total Sales:", total_sales)
print("Average Daily Sales:", average_sales)
print("Standard Deviation of Daily Sales:", std_sales)
#Best-selling product
product_quantity = df.groupby("Product")["Quantity"].sum()
best_product = product_quantity.idxmax()

print("\nBest Selling Product:", best_product)