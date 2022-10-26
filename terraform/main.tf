terraform {
   required_providers {
     aws = {
       source = "hashicorp/aws"
       version = "~>2.0"
     }
   }
}

# Configurando Provider AWS

provider "aws" {
  insecure = true
#  version = "~>2.0"
  region  = "us-east-1"
  }

# Configurando instancia que será criada na AWS 
resource "aws_instance" "poke" {
    count = 1 # Adicione o numero que maquina que deseja criar.
    ami = "ami-0e472ba40eb589f49"
    instance_type = "t2.micro"
    key_name = var.key_name
    tags = {
        name = "poke${count.index}"
    }
    vpc_security_group_ids = ["${aws_security_group.poke-dex-ssh.id}"]

     user_data = <<-EOF
                    #!/bin/bash
                    mkdir /home/ubuntu/pokemon && chown ubuntu:ubuntu /home/ubuntu/pokemon
                    cd /home/ubuntu/pokemon
                    git clone https://github.com/danilospacheco/pokeapi.git
                    EOF
}
