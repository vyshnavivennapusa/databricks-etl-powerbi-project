# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT
# MAGIC     order_status,
# MAGIC     COUNT(order_id) AS total_orders
# MAGIC FROM workspace.default.silver_orders
# MAGIC GROUP BY order_status
# MAGIC ORDER BY total_orders DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     DATE_FORMAT(order_purchase_timestamp, 'yyyy-MM') AS order_month,
# MAGIC     COUNT(order_id) AS total_orders
# MAGIC FROM workspace.default.silver_orders
# MAGIC GROUP BY DATE_FORMAT(order_purchase_timestamp, 'yyyy-MM')
# MAGIC ORDER BY order_month;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     delivery_status,
# MAGIC     COUNT(*) AS total_orders,
# MAGIC     ROUND(AVG(delivery_days), 2) AS avg_delivery_days
# MAGIC FROM workspace.default.silver_orders
# MAGIC GROUP BY delivery_status
# MAGIC ORDER BY total_orders DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     delivery_status,
# MAGIC     MIN(delivery_days) AS min_delivery_days,
# MAGIC     MAX(delivery_days) AS max_delivery_days,
# MAGIC     ROUND(AVG(delivery_days), 2) AS avg_delivery_days
# MAGIC FROM workspace.default.silver_orders
# MAGIC WHERE delivery_days IS NOT NULL
# MAGIC GROUP BY delivery_status;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC ROUND(SUM(payment_value),2) AS total_revenue
# MAGIC FROM workspace.default.gold_sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC DATE_FORMAT(order_purchase_timestamp,'yyyy-MM') AS month,
# MAGIC ROUND(SUM(payment_value),2) AS revenue
# MAGIC FROM workspace.default.gold_sales
# MAGIC GROUP BY DATE_FORMAT(order_purchase_timestamp,'yyyy-MM')
# MAGIC ORDER BY month;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC seller_id,
# MAGIC ROUND(SUM(price),2) AS total_sales
# MAGIC FROM workspace.default.gold_sales
# MAGIC GROUP BY seller_id
# MAGIC ORDER BY total_sales DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC product_category_name,
# MAGIC ROUND(SUM(price),2) AS total_sales
# MAGIC FROM workspace.default.gold_sales
# MAGIC GROUP BY product_category_name
# MAGIC ORDER BY total_sales DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC payment_type,
# MAGIC COUNT(*) AS total_orders,
# MAGIC ROUND(SUM(payment_value),2) AS revenue
# MAGIC FROM workspace.default.gold_sales
# MAGIC GROUP BY payment_type
# MAGIC ORDER BY revenue DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC ROUND(AVG(delivery_days),2) AS avg_delivery_days
# MAGIC FROM workspace.default.gold_sales
# MAGIC WHERE delivery_days IS NOT NULL;

# COMMAND ----------

SHOW TABLES IN workspace.default;