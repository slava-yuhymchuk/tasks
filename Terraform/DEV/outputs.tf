# Outputs definitions

# VPC outputs

output "name" {
  description = "VPC name"
  value       = module.vpc.name
}

output "vpc_id" {
  description = "VPC ID"
  value       = module.vpc.vpc_id
}

output "private_subnets" {
  description = "List of IDs of private subnets"
  value       = module.vpc.private_subnets
}

# EKS outputs

output "cluster_name" {
  description = "Cluster name"
  value       = module.eks.cluster_name
}

output "cluster_id" {
  description = "Cluster ID"
  value       = module.eks.cluster_id
}

output "cluster_version" {
  description = "Cluster version"
  value       = module.eks.cluster_version
}

output "cluster_status" {
  description = "Cluster status"
  value       = module.eks.cluster_status
}

output "eks_managed_node_groups" {
  description = "Node groups"
  value       = module.eks.eks_managed_node_groups
}
