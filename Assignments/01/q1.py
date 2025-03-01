import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("heart_disease.csv")

print(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.\n")
print("Summary statistics:\n", df.describe())

print("\nDepartment-wise employee count:\n", df["Department"].value_counts())
print("\nPromotion Status count:\n", df["Promotion Status"].value_counts())

missing_values = df.isnull().sum()
print("\nMissing values in each column:\n", missing_values)

df["Salary ($)"].fillna(df["Salary ($)"].mean(), inplace=True)
df["Promotion Status"].fillna(df["Promotion Status"].mode()[0], inplace=True)

plt.figure(figsize=(9, 5))
plt.hist(df["Salary ($)"], bins=10, color="orange", edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary ($)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
df["Department"].value_counts().plot(kind="bar", color="pink")
plt.title("Number of Employees by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.grid(axis="y")
plt.show()

plt.figure(figsize=(7, 5))
sns.boxplot(y=df["Experience (Years)"], color="yellow")
plt.title("Experience (Years) Box Plot")
plt.ylabel("Years of Experience")
plt.grid(True)
plt.show()
