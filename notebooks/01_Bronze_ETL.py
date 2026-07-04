# Databricks notebook source
# Read the Orders dataset from the Volume

orders_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/Volumes/workspace/default/retail_data/olist_orders_dataset.csv")

# Display the data
display(orders_df)

# COMMAND ----------

# Total number of rows and columns

print(f"Number of Rows: {orders_df.count()}")
print(f"Number of Columns: {len(orders_df.columns)}")

# COMMAND ----------

# Display the schema

orders_df.printSchema()

# COMMAND ----------

spark.sql("SHOW TABLES IN workspace.default").show()