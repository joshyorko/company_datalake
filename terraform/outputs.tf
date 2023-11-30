output "data_lake_s3_bucket_name" {
  value       = module.data_lake.s3_bucket_name
  description = "The name of the S3 bucket used for the data lake"
}

output "data_lake_s3_bucket_arn" {
  value       = module.data_lake.s3_bucket_arn
  description = "The ARN of the S3 bucket used for the data lake"
}
