variable "glue_database_name" {
  description = "The name of the Glue database"
  type        = string
}

variable "silver_lake_crawler_name" {
  description = "The name of the  silver_lake_crawler_name Glue crawler"
  type        = string
}
variable "gold_lake_crawler_name" {
  description = "The name of the  gold_lake_crawler_name Glue crawler"
  type        = string
} 

variable "s3_target_path_silver" {
  description = "The S3 path for the silver lake"
  type        = string
}

variable "s3_target_path_gold" {
  description = "The S3 path for the gold lake"
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