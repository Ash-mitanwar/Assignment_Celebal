# Databricks notebook source
import pandas as pd

# COMMAND ----------

df = pd.read_csv("/Workspace/Users/ashmitharyana@gmail.com/Drafts/SampleSuperstore.csv", encoding='ISO-8859-1')

# COMMAND ----------

df.head()

# COMMAND ----------

df.tail()

# COMMAND ----------

df.shape

# COMMAND ----------

df.columns

# COMMAND ----------

df.dtypes

# COMMAND ----------

df.info()

# COMMAND ----------

df.isnull()

# COMMAND ----------

df.isnull().sum()

# COMMAND ----------

df.fillna("Unknown")

# COMMAND ----------

df[df["Sales"]>500]

# COMMAND ----------

df[df["Category"] == "Technology"]

# COMMAND ----------

df[["Category", "Profit"]]

# COMMAND ----------

df.duplicated()

# COMMAND ----------

df.duplicated().sum()

# COMMAND ----------

df.drop_duplicates()

# COMMAND ----------

df["Price"] = df["Sales"] / df["Quantity"]
df["Total_Amount"] = df["Price"] * df["Quantity"]

# COMMAND ----------

df.head()

# COMMAND ----------

df.to_csv("/Workspace/Users/ashmitharyana@gmail.com/Cleaned_Superstore.csv", index=False)