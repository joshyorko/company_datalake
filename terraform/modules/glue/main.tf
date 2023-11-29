resource "aws_glue_catalog_database" "example" {
  name = var.database_name
}

resource "aws_glue_crawler" "example" {
  database_name = aws_glue_catalog_database.example.name
  name          = var.crawler_name
  role          = var.iam_role
  s3_target {
    path = var.s3_path
  }
}

resource "aws_glue_job" "example" {
  name     = var.job_name
  role_arn = var.iam_role
  command {
    script_location = var.script_path
    python_version  = "3"
  }
  default_arguments = {
    "--TempDir" = var.temp_dir
  }
}