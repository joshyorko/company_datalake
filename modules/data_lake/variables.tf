variable "bucket_name" {
  description = "The name of the S3 bucket"
  type        = string
}

variable "versioning_enabled" {
  description = "Boolean to enable versioning"
  type        = bool
  default     = true
}

variable "aws_s3_bucket_acl" {
  description = "The ACL to apply to the bucket"
  type        = string
  default     = "private"
}
// Add any additional variables for further configurations

variable "glue_scripts_bucket_name" {
  description = "The name of the S3 bucket"
  type        = string
}