# Variables definitions

variable "profile" {
  description = "AWS authentication profile"
  type        = string
  default     = "slava"
}

variable "region" {
  description = "AWS Region name"
  type        = string
  default     = "il-central-1"
}

variable "env" {
  description = "Environment"
  type        = string
  default     = "dev"
}

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
  default     = "eks-dev"
}

variable "cluster_version" {
  description = "Kubernetes version to use for the EKS cluster"
  type        = string
  default     = "1.30"
}

variable "cluster_endpoint_public_access" {
  description = "Enable public API server endpoint"
  type        = bool
  default     = true
}

variable "vpc_id" {
  description = "VPC ID where to create the cluster"
  type        = string
  default     = null
}

variable "subnet_ids" {
  description = "A list of subnet IDs where the nodes will be provisioned"
  type        = list(string)
  default     = null
}

variable "instance_types" {
  description = "A list of instance types for cluster nodes"
  type        = list(string)
  default     = ["t3.micro"]
}

variable "ami_type" {
  description = "AMI type for cluster nodes"
  type        = string
  default     = "AL2023_x86_64_STANDARD"
}
