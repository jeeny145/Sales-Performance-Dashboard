import os
print("Current Folder:", os.getcwd())
print("Files:", os.listdir())

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100

plt.figure(figsize=(14,8))
plt.subplot(2,2,1)
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.subplot(2,2,2)
plt.plot(df["Month"], df["Profit"], marker='o')
plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.subplot(2,2,3)
plt.bar(df["Month"], df["Orders"])
plt.title("Monthly Orders")
plt.xlabel("Month")
plt.ylabel("Orders")

plt.subplot(2,2,4)
plt.plot(df["Month"], df["Profit_Margin"], marker='o')
plt.title("Profit Margin (%)")
plt.xlabel("Month")
plt.ylabel("Profit Margin")
plt.tight_layout()
plt.show()
print("\n----- Business Insights -----")
print("Highest Sales Month:",
      df.loc[df["Sales"].idxmax(), "Month"])

print("Highest Profit Month:",
      df.loc[df["Profit"].idxmax(), "Month"])
print("Total Sales: ₹", df["Sales"].sum())
print("Total Profit: ₹", df["Profit"].sum())