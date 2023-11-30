output "glue_database_name" {
  value       = aws_glue_catalog_database.database.name
  description = "The name of the created Glue database"
}


output "silver_lake_crawler_name" {
  value       = aws_glue_crawler.silver_lake_crawler.name
  description = "The name of the created Glue crawler"
} 

output "gold_lake_crawler_name" {
  value       = aws_glue_crawler.gold_lake_crawler.name
  description = "The name of the created Glue crawler"
}

output "silver_lake_crawler_arn" {
  value       = aws_glue_crawler.silver_lake_crawler.arn
  description = "The ARN of the created Glue crawler"
}

output "gold_lake_crawler_arn" {
  value       = aws_glue_crawler.gold_lake_crawler.arn
  description = "The ARN of the created Glue crawler"
}

