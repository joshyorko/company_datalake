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

# Hardcoded S3 paths
s3_source = "s3://portfolio-company-datalake-jy/fake-companies"
s3_target = "s3://portfolio-company-datalake-jy/processed-data"  # Update this to your desired target path

# Read CSV data from S3
companies_df = spark.read.option("header", "true").option("inferSchema", "true").csv(s3_source + "/companies/")
employees_df = spark.read.option("header", "true").option("inferSchema", "true").csv(s3_source + "/employees/")
departments_df = spark.read.option("header", "true").option("inferSchema", "true").csv(s3_source + "/departments/")

# Process Data (transformations, cleaning, etc.)

# Write Data to S3 in Parquet format
companies_df.write.mode("overwrite").parquet(s3_target + "/companies/")
employees_df.write.mode("overwrite").parquet(s3_target + "/employees/")
departments_df.write.mode("overwrite").parquet(s3_target + "/departments/")

# Commit the job
job.commit()
