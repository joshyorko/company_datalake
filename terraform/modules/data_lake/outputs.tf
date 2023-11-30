output "s3_bucket_name" {
  value       = aws_s3_bucket.data_lake.bucket
  description = "The name of the S3 bucket used for the data lake"
}

output "s3_bucket_arn" {
  value       = aws_s3_bucket.data_lake.arn
  description = "The ARN of the S3 bucket used for the data lake"
}
