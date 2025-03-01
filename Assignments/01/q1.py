import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Age": [28, 35, 42, 30, 50, 41, 29, 33, 45, 39],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Department": ["IT", "HR", "Finance", "Marketing", "Sales", "HR", "IT", "Finance", "Sales", "Marketing"],
    "Salary ($)": [70000, 60000, 90000, 65000, 85000, 62000, 75000, 88000, 87000, 67000],
    "Experience (Years)": [3, 7, 12, 5, 15, 9, 4, 11, 14, 6],
    "Work Hours/Week": [40, 38, 45, 42, 50, 37, 39, 44, 48, 41],
    "Projects Completed": [5, 4, 6, 7, 8, 5, 6, 7, 9, 6],
    "Job Satisfaction (1-10)": [7, 8, 6, 9, 5, 7, 8, 6, 5, 8],
    "Training Hours": [20, 15, 18, 25, 12, 16, 22, 20, 14, 19],
    "Promotion Status": ["No", "Yes", "Yes", "No", "Yes", "No", "No", "Yes", "Yes", "No"]
}

df = pd.DataFrame(data)

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
