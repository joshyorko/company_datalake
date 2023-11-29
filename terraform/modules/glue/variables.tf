variable "region" {
  description = "The region where the AWS Glue resources will be created"
  type        = string
  default     = "us-west-2"
}

variable "glue_job_name" {
  description = "The name of the AWS Glue job"
  type        = string
}

variable "glue_role_arn" {
  description = "The ARN of the IAM role that AWS Glue can assume to access data in other services"
  type        = string
}

variable "glue_script_location" {
  description = "The S3 location of the AWS Glue ETL script"
  type        = string
}

variable "glue_script_arguments" {
  description = "The arguments that get passed to the AWS Glue ETL script"
  type        = map(string)
  default     = {}
}