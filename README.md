# My Terraform Project

This project contains the Terraform configuration files for setting up an AWS Glue and a data lake. The project also includes a Python script for creating a company.

## Project Structure

The project has the following structure:

- `main.tf`: Main Terraform configuration file.
- `variables.tf`: File for declaring variables used in `main.tf`.
- `outputs.tf`: File for declaring outputs of the Terraform configuration.
- `scripts/company.py`: Python script for creating a company.
- `modules/glue`: Directory for the AWS Glue module.
- `modules/data_lake`: Directory for the data lake module.

Each module directory contains its own `main.tf`, `variables.tf`, and `outputs.tf` files.

## Usage

To use this project, follow these steps:

1. Clone the repository.
2. Navigate to the project directory.
3. Run `terraform init` to initialize the project.
4. Run `terraform plan` to see the changes that will be made.
5. Run `terraform apply` to apply the changes.

Please ensure that you have the necessary AWS credentials set up in your environment before running the Terraform commands.

## Note

The Python script `scripts/company.py` is not directly related to the Terraform configuration. It should be run separately, depending on your needs.