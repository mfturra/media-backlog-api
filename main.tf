terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

region {
    default     = "us-east-2"
    description = "AWS region"
}

provider "aws" {
  region  = "us-east-2"
}

resource "aws_instance" "media_backlog_api" {
    ami           = "ami-053b0d53c279acc90"
    instance_type = "t2.micro"

    key_name = var.vs-flask-1.cer
    
    # root disk
    root_block_device {
      volume_size = "8"
      volume_type = "gp2"
      encrypted = true
    }
}

module "vpc" {
    source              = "terraform-aws-modules/vpc/aws"
    version             = "2.66.0"
    
    //name = "media-backlog-vpc"
    //cidr = "10.0.0.0/16"
    vpc_security_group_ids = [aws_security_group.sg-03f65b38a1d081a4f]
}

resource "aws_security_group" "flask_web_server_sec_group" {
    name_prefix         = "flask_web_server_sec_group"
    vpc_id              = module.vpc.vpc-02b3bc3edb2dc2583

    ingress {
        from_port       = 22
        to_port         = 22
        protocol        = "tcp"
        cidr_blocks     = [
            "0.0.0.0/0",
            ]
    }

    ingress {
        from_port       = 80
        to_port         = 80
        protocol        = "tcp"
        cidr_blocks     = ["0.0.0.0/0"]
    }

    ingress {
        from_port       = 443
        to_port         = 443
        protocol        = "tcp"
        cidr_blocks     = ["0.0.0.0/0"]
    }

    ingress {
        from_port       = 5000
        to_port         = 5000
        protocol        = "tcp"
        cidr_blocks     = ["0.0.0.0/0"]
    }
}