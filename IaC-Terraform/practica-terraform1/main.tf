provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "platzi-instance" {
  ami           = "ami-08bf7fc6ae9c06046"
  instance_type = "t2.micro"
  tags = {
    Name = "practica1"
    Env  = "Dev"
  }
}