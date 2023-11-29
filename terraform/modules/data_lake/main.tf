resource "aws_s3_bucket" "data_lake_bucket" {
  bucket = var.bucket_name
  acl    = "private"

  versioning {
    enabled = true
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "aws:kms"
        kms_master_key_id = aws_kms_key.data_lake_key.arn
      }
    }
  }
}

resource "aws_kms_key" "data_lake_key" {
  description             = "KMS key for data lake bucket"
  deletion_window_in_days = 7
}

variable "bucket_name" {
  description = "The name of the bucket to create for the data lake"
  type        = string
}