variable "region" {
  description = "AWS Region"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "Name of the S3 bucket for data lake"
  type        = string
}

variable "versioning_enabled" {
  description = "Boolean to enable versioning for the S3 bucket"
  type        = bool
  default     = true
}

variable "glue_database_name" {
  description = "Name of the AWS Glue database"
  type        = string
}

variable "silver_lake_crawler" {
  description = "Name of the silver_lake_crawler Glue crawler"
  type        = string
}

variable "gold_lake_crawler" {
  description = "Name of the gold_lake_crawler Glue crawler"
  type        = string
}
variable "s3_target_path_silver" {
  description = "S3 target path for silver lake"
  type        = string
}

variable "s3_target_path_gold" {
  description = "S3 target path for gold lake"
  type        = string
}


variable "glue_iam_role_name" {
  description = "The name of the IAM role for AWS Glue"
  type        = string
}

variable "glue_policy_name" {
  description = "The name of the IAM policy for AWS Glue"
  type        = string
}

variable "aws_s3_bucket_acl" {
  description = "The ACL for the S3 bucket"
  type        = string
  default     = "private"
}

variable "glue_scripts_bucket_name" {
  description = "The name of the S3 bucket for AWS Glue scripts"
  type        = string
}