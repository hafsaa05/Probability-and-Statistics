import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("heart_disease.csv")

print(f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")
print("\nSummary Statistics:\n", df.describe())
print("\nGender Distribution:\n", df["Gender"].value_counts())
print("\nSmoking Distribution:\n", df["Smoking"].value_counts())

missing_values = df.isnull().sum()
print("\nMissing Values per Column:\n", missing_values[missing_values > 0])

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Cholesterol Level"] = df["Cholesterol Level"].fillna(df["Cholesterol Level"].mean())
df["Smoking"] = df["Smoking"].fillna(df["Smoking"].mode()[0])

heart_disease_col = [col for col in df.columns if "Heart Disease" in col]
if heart_disease_col:
    heart_disease_col = heart_disease_col[0]
else:
    raise KeyError("Column 'Heart Disease' not found! Check dataset columns.")

plt.figure(figsize=(10, 6))
plt.hist(df["Age"], bins=20, color="orange", edgecolor="black", alpha=0.8)
plt.title("Age Distribution", fontsize=14)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

plt.figure(figsize=(9, 5))
heart_disease_counts = df[heart_disease_col].value_counts()
plt.bar(heart_disease_counts.index, heart_disease_counts.values, color=["pink", "red"])
plt.xticks(ticks=[0, 1], labels=["No Disease", "Disease"], fontsize=12)
plt.title("Heart Disease Cases", fontsize=14)
plt.xlabel("Condition", fontsize=12)
plt.ylabel("People", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

plt.figure(figsize=(8, 4))
sns.boxplot(y=df["Cholesterol Level"], color="purple")
plt.title("Cholesterol Levels", fontsize=14)
plt.ylabel("Cholesterol", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

if "Salary" in df.columns:
    plt.figure(figsize=(10, 6))
    plt.hist(df["Salary"], bins=15, color="yellow", edgecolor="black", alpha=0.8)
    plt.title("Salary Distribution", fontsize=14)
    plt.xlabel("Salary", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
else:
    print("\n'Salary' column not found in the dataset!")

if "Department" in df.columns:
    plt.figure(figsize=(9, 5))
    department_counts = df["Department"].value_counts()
    plt.bar(department_counts.index, department_counts.values, color="purple")
    plt.xticks(rotation=45, fontsize=12)
    plt.title("Employees per Department", fontsize=14)
    plt.xlabel("Department", fontsize=12)
    plt.ylabel("Number of Employees", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
else:
    print("\n'Department' column not found in the dataset!")

if "Experience (Years)" in df.columns:
    plt.figure(figsize=(8, 4))
    sns.boxplot(y=df["Experience (Years)"], color="red")
    plt.title("Experience (Years) Distribution", fontsize=14)
    plt.ylabel("Years of Experience", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
else:
    print("\n'Experience (Years)' column not found in the dataset!")
