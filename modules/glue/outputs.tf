output "glue_database_name" {
  value       = aws_glue_catalog_database.database.name
  description = "The name of the created Glue database"
}

output "glue_crawler_name" {
  value       = aws_glue_crawler.crawler.name
  description = "The name of the created Glue crawler"
}

output "glue_crawler_arn" {
  value       = aws_glue_crawler.crawler.arn
  description = "The ARN of the created Glue crawler"
}
