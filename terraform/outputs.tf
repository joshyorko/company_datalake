output "glue_output" {
  description = "Output from the AWS Glue module"
  value       = module.glue.some_output
}

output "data_lake_output" {
  description = "Output from the Data Lake module"
  value       = module.data_lake.some_output
}