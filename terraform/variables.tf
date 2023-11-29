variable "aws_region" {
  description = "The AWS region where resources will be created"
  type        = string
  default     = "us-west-2"
}

variable "glue_job_name" {
  description = "The name of the AWS Glue job"
  type        = string
}

variable "data_lake_name" {
  description = "The name of the data lake"
  type        = string
}