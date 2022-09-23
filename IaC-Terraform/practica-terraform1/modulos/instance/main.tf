provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "platzi-instance" {
  ami             = var.ami_id
  instance_type   = var.instance_type
  tags            = var.tags
  security_groups = ["${aws_security_group.ssh_connection.name}"]
  provisioner "remote-exec" {
    connection {
      type        = "ssh"
      user        = "admin"
      private_key = file("~/estudio/Platzi/IaC-Terraform/demo-packer/scripts/packer-key.pub")
      host        = self.public_ip
    }
    inline = ["echo hello", "docker run -it -d -p 80:80 ajinomano/hello-platzi:v1"]
  }
}

resource "aws_security_group" "ssh_connection" {
  name = var.sg_name

  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.from_port
      to_port     = ingress.value.to_port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
    }
  }

  # dynamic "egress" {
  #   for_each = var.egress_rules
  #   content {
  #     from_port   = egress.value.from_port
  #     to_port     = egress.value.to_port
  #     protocol    = egress.value.protocol
  #     cidr_blocks = egress.value.cidr_blocks
  #   }
  # }
}