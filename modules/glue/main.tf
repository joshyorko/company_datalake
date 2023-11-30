resource "aws_glue_catalog_database" "database" {
  name = var.glue_database_name
  // Optionally, you can add more configurations here
}

resource "aws_glue_crawler" "crawler" {
  name         = var.crawler_name
  database_name = aws_glue_catalog_database.database.name

  s3_target {
    path = var.s3_target_path
  }

  role = var.glue_service_role_arn
  // Additional configurations can be added as needed
}
