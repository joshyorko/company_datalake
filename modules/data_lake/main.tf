resource "aws_s3_bucket" "data_lake" {
  bucket = var.bucket_name
  // ... other configurations ...
}

resource "aws_s3_bucket" "glue_scripts_bucket" {
  bucket = var.glue_scripts_bucket_name
  // Other configurations...

  provisioner "local-exec" {
  command = "aws s3 cp ../../scripts/glue-jobs/ s3://${self.bucket}/glue-jobs/ --recursive"
    }

}


resource "aws_s3_bucket_lifecycle_configuration" "data_lake_lifecycle" {
  bucket = aws_s3_bucket.data_lake.id

  rule {
    id      = "log"
    status  = "Enabled"  # Replaces the 'enabled' field

    filter {
      prefix = "logs/"
    }

    transition {
      days          = 30
      storage_class = "STANDARD_IA" 
    }

    expiration {
      days = 365
    }
  }

  # ... other rules if needed ...
}
