# Databricks notebook source
orders_df = spark.table("workspace.default.silver_orders")

display(orders_df)

# COMMAND ----------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pdf = orders_df.toPandas()

pdf.head()

# COMMAND ----------

pdf.info()

# COMMAND ----------

pdf.describe(include="all")

# COMMAND ----------

pdf.isnull().sum()

# COMMAND ----------

pdf["order_status"].value_counts()

# COMMAND ----------

plt.figure(figsize=(8,5))
pdf["order_status"].value_counts().plot(kind="bar")
plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Count")
plt.show()

# COMMAND ----------

plt.figure(figsize=(8,5))
pdf["delivery_days"].dropna().hist(bins=30)
plt.title("Delivery Days Distribution")
plt.xlabel("Delivery Days")
plt.ylabel("Frequency")
plt.show()

# COMMAND ----------

pdf["order_purchase_timestamp"] = pd.to_datetime(pdf["order_purchase_timestamp"])

monthly_orders = (
    pdf.groupby(pdf["order_purchase_timestamp"].dt.to_period("M"))
       .size()
)

monthly_orders.index = monthly_orders.index.astype(str)
monthly_orders

# COMMAND ----------

plt.figure(figsize=(12,5))
monthly_orders.plot()
plt.title("Monthly Orders")
plt.xlabel("Month")
plt.ylabel("Orders")
plt.xticks(rotation=45)
plt.show()

# COMMAND ----------

pdf.groupby("delivery_status")["delivery_days"].agg(["count","mean","min","max"])

# COMMAND ----------

customers_df = spark.read.format("csv") \
.option("header","true") \
.option("inferSchema","true") \
.load("/Volumes/workspace/default/retail_data/olist_customers_dataset.csv")

customers_df.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("workspace.default.silver_customers")

# COMMAND ----------

products_df = spark.read.format("csv") \
.option("header","true") \
.option("inferSchema","true") \
.load("/Volumes/workspace/default/retail_data/olist_products_dataset.csv")

products_df.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("workspace.default.silver_products")

# COMMAND ----------

order_items_df = spark.read.format("csv") \
.option("header","true") \
.option("inferSchema","true") \
.load("/Volumes/workspace/default/retail_data/olist_order_items_dataset.csv")

order_items_df.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("workspace.default.silver_order_items")

# COMMAND ----------

payments_df = spark.read.format("csv") \
.option("header","true") \
.option("inferSchema","true") \
.load("/Volumes/workspace/default/retail_data/olist_order_payments_dataset.csv")

payments_df.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("workspace.default.silver_payments")

# COMMAND ----------

sellers_df = spark.read.format("csv") \
.option("header","true") \
.option("inferSchema","true") \
.load("/Volumes/workspace/default/retail_data/olist_sellers_dataset.csv")

sellers_df.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("workspace.default.silver_sellers")

# COMMAND ----------

spark.sql("SHOW TABLES IN workspace.default").show()