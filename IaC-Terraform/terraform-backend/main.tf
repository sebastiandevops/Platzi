provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "platzi-backend" {
  bucket = var.bucket_name
  tags   = var.tags

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        kms_master_key_id = aws_kms_key.mykey.arn
        sse_algorithm     = "aws:kms"
      }
    }
  }
}

resource "aws_s3_bucket_acl" "platzi-backend-acl" {
  bucket = aws_s3_bucket.platzi-backend.id
  acl    = var.acl
}

resource "aws_kms_key" "mykey" {
  description             = "This key is used to encrypt bucket objects"
  deletion_window_in_days = 10
}

output "arn" {
  value = aws_kms_key.mykey.arn
}