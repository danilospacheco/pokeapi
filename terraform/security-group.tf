resource "aws_security_group" "poke-dex-ssh" {
  name        = "poke-dex-ssh"
  description = "Resource group criado para o projeto pokeApi"
  #vpc_id      = aws_vpc.main.id

  # Regra de entrada
  ingress {
    description      = "TLS from VPC"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = var.cdirs_acesso_remoto
    #cidr_blocks      = ["0.0.0.0/0"]
    #ipv6_cidr_blocks = [aws_vpc.main.ipv6_cidr_block]
    
  }

  # Regra de saida
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
   # ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "ssh"
  }
}