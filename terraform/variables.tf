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

variable "crawler_name" {
  description = "Name of the Glue crawler"
  type        = string
}

variable "s3_target_path" {
  description = "The S3 path to be crawled"
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

