variable "data_lake_name" {
  description = "The name of the data lake"
  type        = string
}

variable "data_lake_storage" {
  description = "The amount of storage for the data lake in GB"
  type        = number
}

variable "data_lake_region" {
  description = "The AWS region where the data lake should be created"
  type        = string
}