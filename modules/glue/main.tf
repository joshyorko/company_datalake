resource "aws_glue_catalog_database" "database" {
  name = var.glue_database_name
  // Optionally, you can add more configurations here
}

resource "aws_glue_crawler" "silver_lake_crawler" {
  name         = var.silver_lake_crawler_name
  database_name = aws_glue_catalog_database.database.name

  s3_target {
    path = var.s3_target_path_silver
  }

  role = var.glue_service_role_arn
  // Additional configurations can be added as needed
}

resource "aws_glue_crawler" "gold_lake_crawler" {
  name         = var.gold_lake_crawler_name
  database_name = aws_glue_catalog_database.database.name

  s3_target {
    path = var.s3_target_path_gold
  }

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

  # Other configurations...
}
