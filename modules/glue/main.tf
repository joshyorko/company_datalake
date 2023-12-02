resource "aws_glue_catalog_database" "database" {
  name = var.glue_database_name
  // Optionally, you can add more configurations here
  description = "This AWS Glue database 'database' is responsible for storing metadata for the Bronze, Silver, and Gold data layers."
}

resource "aws_glue_crawler" "silver_lake_crawler" {
  name         = var.silver_lake_crawler_name
  database_name = aws_glue_catalog_database.database.name

  s3_target {
    path = var.s3_target_path_silver
  }

  role = var.glue_service_role_arn

  description = "This AWS Glue crawler 'silver-lake-crawler' is responsible for updating the metadata catalog in the Silver data layer. It crawls the S3 bucket 's3://${var.s3_target_path_silver}' and updates the metadata catalog accordingly."
  // Additional configurations can be added as needed
}

resource "aws_glue_crawler" "gold_lake_crawler" {
  name         = var.gold_lake_crawler_name
  database_name = aws_glue_catalog_database.database.name

  s3_target {
    path = var.s3_target_path_gold
  }
  description = "This AWS Glue crawler 'gold-lake-crawler' is responsible for updating the metadata catalog in the Gold data layer. It crawls the S3 bucket 's3://${var.s3_target_path_gold}' and updates the metadata catalog accordingly."
  role = var.glue_service_role_arn
  // Additional configurations can be added as needed
}

resource "aws_glue_job" "gold_lake_job" {
  name       = "gold-lake-job"
  role_arn   = var.glue_service_role_arn
  glue_version = "4.0"  # Specify the Glue version here

  command {
    script_location = "s3://${var.glue_scripts_bucket_name}/glue-jobs/gold_lake.py"
    python_version  = "3"
  }

   description = "This AWS Glue job 'gold-lake-job' is responsible for transforming and optimizing Parquet data from the Silver data layer and writing it to the Gold data layer. Key operations include [mention specific transformations or optimizations, if any]. The job ensures data is stored in Parquet format with efficient partitioning. Post-processing, it triggers a Glue Crawler to refresh metadata in the Gold layer."

  # Other configurations...
}

resource "aws_glue_job" "silver_lake_job" {
  name       = "silver-lake-job"
  role_arn   = var.glue_service_role_arn
  glue_version = "4.0"  # Specify the Glue version here

  command {
    script_location = "s3://${var.glue_scripts_bucket_name}/glue-jobs/silver_lake.py"
    python_version  = "3"
  }
  description = "This AWS Glue job 'silver-lake-job' processes and transforms data from the Bronze data layer for storage in the Silver data layer. Key transformations include deduplication in the 'Name' column of the 'companies' DataFrame. The job writes the processed data to specific directories within the Silver layer and triggers a Glue Crawler to update the metadata catalog accordingly."
  # Other configurations...
}
