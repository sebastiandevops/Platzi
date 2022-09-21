variable "bucket_name" {
  default = "backend-terraform-platzi-726"
}
variable "acl" {
  default = "private"
}
variable "tags" {
  default = { Environment = "Dev", "CreatedBy" = "terraform" }
}