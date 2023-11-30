import sys
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions

# Initialize Glue and Spark contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Parameters
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_SILVER_SOURCE', 'S3_GOLD_TARGET'])

# Define job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read Parquet data from Silver layer
companies_df = spark.read.parquet(args['S3_SILVER_SOURCE'] + "/companies/")
employees_df = spark.read.parquet(args['S3_SILVER_SOURCE'] + "/employees/")
departments_df = spark.read.parquet(args['S3_SILVER_SOURCE'] + "/departments/")

# Additional transformations or optimizations
# e.g., companies_df = companies_df.withColumnRenamed("employees", "num_employees")

# Partitioning and writing data to the Gold layer in Parquet format
# Example partitioning: companies by 'Industry', employees by 'Company_Name', departments by 'Location'

companies_df.write.mode("overwrite").partitionBy("Industry").parquet(args['S3_GOLD_TARGET'] + "/companies/")
employees_df.write.mode("overwrite").partitionBy("Company_Name").parquet(args['S3_GOLD_TARGET'] + "/employees/")
departments_df.write.mode("overwrite").partitionBy("Location").parquet(args['S3_GOLD_TARGET'] + "/departments/")

# Commit the job
job.commit()
