output "glue_job_name" {
  description = "The name of the Glue job"
  value       = aws_glue_job.example.name
}

output "glue_job_role_arn" {
  description = "The ARN of the IAM role associated with the Glue job"
  value       = aws_glue_job.example.role_arn
}