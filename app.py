from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("EmployeeRDDProject") \
    .getOrCreate()

sc = spark.sparkContext

# Read CSV
rdd = sc.textFile("data/employees.csv")

header = rdd.first()

employees = rdd.filter(lambda x: x != header) \
               .map(lambda x: x.split(","))

# -----------------------------------
# Sort employees by salary descending
# -----------------------------------

sorted_employees = employees.sortBy(
    lambda x: int(x[3]),
    ascending=False
)

print("\n===== Employees Sorted By Salary =====")

for emp in sorted_employees.collect():
    print(emp)

# -----------------------------------
# Department wise salary total
# -----------------------------------

dept_salary = employees.map(
    lambda x: (x[2], int(x[3]))
)

dept_totals = dept_salary.reduceByKey(
    lambda a, b: a + b
)

print("\n===== Department Wise Salary =====")

for row in dept_totals.collect():
    print(row)

# -----------------------------------
# Top 3 highest paid employees
# -----------------------------------

top3 = sorted_employees.take(3)

output_rdd = sc.parallelize(
    [",".join(emp) for emp in top3]
)

output_rdd.saveAsTextFile(
    "output/top3_employees"
)

print("\n===== Top 3 Employees =====")

for emp in top3:
    print(emp)

spark.stop()