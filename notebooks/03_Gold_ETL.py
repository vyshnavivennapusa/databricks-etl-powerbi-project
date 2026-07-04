# Databricks notebook source
from pyspark.sql import functions as F

orders_silver = spark.table("workspace.default.silver_orders")

display(orders_silver)

# COMMAND ----------

orders = spark.table("workspace.default.silver_orders")
customers = spark.table("workspace.default.silver_customers")
order_items = spark.table("workspace.default.silver_order_items")

# COMMAND ----------

gold_orders = orders_silver.groupBy("order_status").agg(
    F.count("order_id").alias("total_orders")
)

display(gold_orders)

# COMMAND ----------

gold_orders.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.default.gold_order_status_summary")

# COMMAND ----------

orders = spark.table("workspace.default.silver_orders")
customers = spark.table("workspace.default.silver_customers")
order_items = spark.table("workspace.default.silver_order_items")
products = spark.table("workspace.default.silver_products")
payments = spark.table("workspace.default.silver_payments")
sellers = spark.table("workspace.default.silver_sellers")

# COMMAND ----------

gold_sales = orders.alias("o") \
.join(customers.alias("c"),
      "customer_id",
      "left") \
.join(order_items.alias("oi"),
      "order_id",
      "left") \
.join(products.alias("p"),
      "product_id",
      "left") \
.join(payments.alias("pay"),
      "order_id",
      "left") \
.join(sellers.alias("s"),
      "seller_id",
      "left")

display(gold_sales)

# COMMAND ----------

gold_sales.printSchema()

# COMMAND ----------

gold_sales.count()

# COMMAND ----------

gold_sales.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("workspace.default.gold_sales")

# COMMAND ----------

display(spark.table("workspace.default.gold_sales"))

# COMMAND ----------

gold_sales.write.format("delta").mode("overwrite").saveAsTable("workspace.default.gold_sales")

# COMMAND ----------

gold_sales_df = spark.table("workspace.default.gold_sales")

gold_sales_df.write \
.format("csv") \
.mode("overwrite") \
.option("header", "true") \
.save("/Volumes/workspace/default/retail_data/gold_sales_export")

# COMMAND ----------

gold_sales = spark.table("workspace.default.gold_sales")

display(gold_sales)