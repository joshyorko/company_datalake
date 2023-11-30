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
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Define job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Hardcoded S3 paths for Silver and Gold layers
s3_silver_source = "s3://portfolio-company-datalake-jy/silver-data"
s3_gold_target = "s3://portfolio-company-datalake-jy/gold-data"

# Read Parquet data from Silver layer
companies_df = spark.read.parquet(s3_silver_source + "/companies/")
employees_df = spark.read.parquet(s3_silver_source + "/employees/")
departments_df = spark.read.parquet(s3_silver_source + "/departments/")

# Additional transformations or optimizations
# e.g., companies_df = companies_df.withColumnRenamed("employees", "num_employees")

# Partitioning and writing data to the Gold layer in Parquet format
# Example partitioning: companies by 'Industry', employees by 'Company_Name', departments by 'Location'
companies_df.write.mode("overwrite").partitionBy("Industry").parquet(s3_gold_target + "/companies/")
employees_df.write.mode("overwrite").partitionBy("Company_Name").parquet(s3_gold_target + "/employees/")
departments_df.write.mode("overwrite").partitionBy("Location").parquet(s3_gold_target + "/departments/")

# Commit the job
job.commit()
