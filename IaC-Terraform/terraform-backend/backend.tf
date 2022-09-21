terraform {
  backend "s3" {
    bucket = "backend-terraform-platzi-726"
    key    = "dev"
    region = "us-east-1"
    encrypt = true
    kms_key_id = "arn:aws:kms:us-east-1:771586990585:key/386e6d30-fed5-4fd8-a597-3023ab135dc8"
    force_destroy = true
  }
}
