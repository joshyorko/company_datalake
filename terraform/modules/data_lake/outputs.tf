output "data_lake_bucket_name" {
  description = "The name of the S3 bucket used for the data lake"
  value       = aws_s3_bucket.data_lake_bucket.bucket
}

output "data_lake_bucket_arn" {
  description = "The ARN of the S3 bucket used for the data lake"
  value       = aws_s3_bucket.data_lake_bucket.arn
}