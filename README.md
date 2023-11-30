# AWS Glue and Data Lake Terraform Project

This project contains Terraform configuration files for setting up an AWS Glue and a data lake. It also includes Python and Go scripts for creating a company and managing AWS resources.

## Project Structure

- `main.tf`: Main Terraform configuration file.
- `variables.tf`: File for declaring variables used in `main.tf`.
- `outputs.tf`: File for declaring outputs of the Terraform configuration.
- `terraform.tfvars`: File for setting values for the declared variables.
- `modules/`: Directory containing the AWS Glue, IAM, and data lake modules. Each module has its own `main.tf`, `variables.tf`, and `outputs.tf` files.
- `scripts/`: Directory containing Python and Go scripts for creating a company and managing AWS resources.

## Usage

1. Clone the repository.
2. Navigate to the project directory.
3. Run `terraform init` to initialize the project.
4. Run `terraform plan` to see the changes that will be made.
5. Run `terraform apply` to apply the changes.

Please ensure that you have the necessary AWS credentials set up in your environment before running the Terraform commands.

## Python and Go Scripts

The Python and Go scripts in the `scripts/` directory are not directly related to the Terraform configuration. They should be run separately, depending on your needs. Please ensure that you have the necessary dependencies installed as specified in the `requirements.txt` and `go.mod` files.

## Note

This project is set up to ignore Python cache files and virtual environments as specified in the `.gitignore` file.