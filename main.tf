# Defining the AWS provider block

provider "aws" {
  region = "us-west-2"  
}

# Defining the VPC
resource "aws_vpc" "VPC" {
  cidr_block = "10.0.0.0/16"  
}

# Defining a subnet within the VPC
resource "aws_subnet" "SUBNET" {
  vpc_id     = aws_vpc.VPC.id  
  cidr_block = "10.0.1.0/24"    
}

# Defining a security group for the EC2 instance
resource "aws_security_group" "SECUITY_GROUP" {
  vpc_id = aws_vpc.VPC.id 

  # Defining ingress rules (inbound traffic)
  ingress {
    from_port   = 22           # SSH
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80           # HTTP
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


# Defining the EC2 instance
resource "aws_instance" "INSTANCE" {
  ami           = "ami-0c55b159cbfafe1f0"  
  instance_type = "t2.micro"               
  subnet_id     = aws_subnet.SUBNET.id 
  key_name      = "KEY_01"   
  vpc_security_group_ids = [aws_security_group.SECUITY_GROUP.id]  

  # Installing necessary software using a provisioner

  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y apache2"  # Install Apache web server
    ]
  }
}
