provider "aws" {
  region = var.region
}

module "iam_for_glue" {
  source         = "./modules/iam"
  iam_role_name  = var.glue_iam_role_name
  policy_name = var.glue_policy_name
}

module "glue" {
  source                = "./modules/glue"
  glue_database_name    = var.glue_database_name
  silver_lake_crawler_name = var.silver_lake_crawler
  gold_lake_crawler_name = var.gold_lake_crawler
  s3_target_path_silver = var.s3_target_path_silver
  s3_target_path_gold = var.s3_target_path_gold
  glue_service_role_arn = module.iam_for_glue.glue_role_arn
  glue_scripts_bucket_name = var.glue_scripts_bucket_name
}

module "data_lake" {
  source             = "./modules/data_lake"
  bucket_name        = var.bucket_name
  versioning_enabled = var.versioning_enabled
  aws_s3_bucket_acl  = var.aws_s3_bucket_acl
  glue_scripts_bucket_name = var.glue_scripts_bucket_name

}
