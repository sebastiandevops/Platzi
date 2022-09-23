ami_id        = "ami-08bf7fc6ae9c06046"
instance_type = "t2.micro"
tags          = { Name = "practica1", Environment = "Prod" }
sg_name       = "platzi-rules"
ingress_rules = [
  {
    from_port   = "22"
    to_port     = "22"
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  },
  {
    from_port   = "80"
    to_port     = "80"
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
]
# egress_rules = [
#   {
#     from_port   = "0"
#     to_port     = "0"
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
# ]