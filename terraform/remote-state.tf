## Using a single workspace:
#terraform {
#  backend "remote" {
#    hostname = "app.terraform.io"
#    organization = "pokemonlabs"
#
#    workspaces {
#      name = "aws-pokemonlabs"
#    }
#  }
#}