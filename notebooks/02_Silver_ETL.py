# Databricks notebook source
from pyspark.sql.functions import *

orders_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/Volumes/workspace/default/retail_data/olist_orders_dataset.csv")

display(orders_df)

# COMMAND ----------

from pyspark.sql.functions import col, when, count

orders_df.select([
    count(when(col(c).isNull(), c)).alias(c)
    for c in orders_df.columns
]).show()

# COMMAND ----------

orders_df.groupBy("order_status") \
    .count() \
    .orderBy(col("count").desc()) \
    .show()

# COMMAND ----------

# Total records
total_records = orders_df.count()

# Unique order IDs
unique_orders = orders_df.select("order_id").distinct().count()

print(f"Total Records : {total_records}")
print(f"Unique Orders : {unique_orders}")
print(f"Duplicate Records : {total_records - unique_orders}")

# COMMAND ----------

orders_df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import datediff

orders_silver = orders_df.withColumn(
    "delivery_days",
    datediff("order_delivered_customer_date", "order_purchase_timestamp")
)

display(orders_silver)

# COMMAND ----------

from pyspark.sql.functions import when

orders_silver = orders_silver.withColumn(
    "delivery_status",
    when(orders_silver.order_status == "delivered", "Delivered")
    .when(orders_silver.order_status == "canceled", "Cancelled")
    .otherwise("Pending")
)

display(orders_silver)

# COMMAND ----------

from pyspark.sql.functions import current_timestamp

orders_silver = orders_silver.withColumn(
    "etl_load_timestamp",
    current_timestamp()
)

display(orders_silver)

# COMMAND ----------

orders_silver.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.default.silver_orders")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC
# MAGIC SELECT *
# MAGIC FROM workspace.default.silver_orders
# MAGIC LIMIT 10;

# COMMAND ----------

orders_df = spark.table("workspace.default.silver_orders")