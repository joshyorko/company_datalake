variable "glue_database_name" {
  description = "The name of the Glue database"
  type        = string
}

variable "crawler_name" {
  description = "The name of the Glue crawler"
  type        = string
}

variable "s3_target_path" {
  description = "The S3 path to be crawled"
  type        = string
}

variable "glue_service_role_arn" {
  description = "The ARN of the IAM role for the Glue service"
  type        = string
}

variable "glue_scripts_bucket_name" {
  description = "The name of the S3 bucket for Glue scripts"
  type        = string
}