from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("SalesDataFrameProject") \
    .getOrCreate()

# Read CSV into DataFrame
df = spark.read.csv(
    "data/sales.csv",
    header=True,
    inferSchema=True
)

print("\n===== Original Data =====")
df.show()

# ----------------------------------
# Sort by Sales Descending
# ----------------------------------

print("\n===== Products Sorted By Sales =====")

sorted_df = df.orderBy(
    col("sales").desc()
)

sorted_df.show()

# ----------------------------------
# Top 3 Highest Sales Products
# ----------------------------------

print("\n===== Top 3 Products =====")

top3 = sorted_df.limit(3)

top3.show()

# ----------------------------------
# Products with Sales > 80000
# ----------------------------------

high_sales = df.filter(
    col("sales") > 80000
)

print("\n===== Sales Greater Than 80000 =====")

high_sales.show()

# Save output as CSV
high_sales.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("output/high_sales_products")

spark.stop()