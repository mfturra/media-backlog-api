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

  tags = {
    Name = "MediaBacklogAPI"
  }
}

