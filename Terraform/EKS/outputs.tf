# Outputs definitions

output "cluster_name" {
  description = "Cluster name"
  value = module.eks.cluster_name
}

output "cluster_id" {
  description = "Cluster ID"
  value = module.eks.cluster_id
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
