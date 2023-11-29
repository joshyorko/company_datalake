provider "aws" {
  region = var.region
}

module "glue" {
  source = "./modules/glue"
  some_variable = var.some_variable
}

module "data_lake" {
  source = "./modules/data_lake"
  another_variable = var.another_variable
}