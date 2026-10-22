import pandas as pd
import matplotlib.pyplot as plt

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
print("Rows, columns:", df.shape)

# Data cleaning
df["Age"] = df["Age"].fillna(df["Age"].median())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df = df.drop(columns=["Cabin"])

df.to_csv("titanic_clean.csv", index=False)

print("Missing values left:", df.isna().sum().sum())

# Analysis
print("Overall survival rate:", round(df["Survived"].mean(), 3))

for column in ["Sex", "Pclass", "Embarked"]:
    rate = df.groupby(column)["Survived"].mean()
    print(rate)

    plt.figure()
    plt.bar(rate.index.astype(str), rate.values)
    plt.title(f"Survival Rate by {column}")
    plt.xlabel(column)
    plt.ylabel("Survival Rate")
    plt.savefig(f"survival_by_{column.lower()}.png")
    plt.close()