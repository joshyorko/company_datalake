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
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_SOURCE', 'S3_TARGET'])

# Define job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read CSV data from S3
companies_df = spark.read.option("header", "true").option("inferSchema", "true").csv(args['S3_SOURCE'] + "/companies/data.csv")
employees_df = spark.read.option("header", "true").option("inferSchema", "true").csv(args['S3_SOURCE'] + "/employees/data.csv")
departments_df = spark.read.option("header", "true").option("inferSchema", "true").csv(args['S3_SOURCE'] + "/departments/data.csv")

# Process Data (transformations, cleaning, etc.)
# Example: companies_df = companies_df.dropDuplicates()

# Write Data to S3 in Parquet format
companies_df.write.mode("overwrite").parquet(args['S3_TARGET'] + "/companies/")
employees_df.write.mode("overwrite").parquet(args['S3_TARGET'] + "/employees/")
departments_df.write.mode("overwrite").parquet(args['S3_TARGET'] + "/departments/")

# Commit the job
job.commit()
