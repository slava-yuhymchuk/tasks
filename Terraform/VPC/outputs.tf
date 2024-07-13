# Outputs definitions

output "name" {
  description = "VPC name"
  value = module.vpc.name
}

output "vpc_id" {
  description = "VPC ID"
  value = module.vpc.vpc_id
}

output "private_subnets" {
  description = "List of IDs of private subnets"
  value       = module.vpc.private_subnets
}
