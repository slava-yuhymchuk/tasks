# Configure AWS provider
provider "aws" {
  profile = var.profile
  region  = var.region
}

# Configure EKS module
module "eks" {
  source = "terraform-aws-modules/eks/aws"

  cluster_name    = "eks-${var.env}"
  cluster_version = var.cluster_version

  cluster_endpoint_public_access = var.cluster_endpoint_public_access

  cluster_addons = {
    coredns                = {}
    eks-pod-identity-agent = {}
    kube-proxy             = {}
    vpc-cni                = {}
  }

  vpc_id     = var.vpc_id
  subnet_ids = var.subnet_ids

  eks_managed_node_group_defaults = {
    instance_types = ["t3.micro"]
  }

  eks_managed_node_groups = {
    (var.cluster_name) = {
      ami_type       = "AL2023_x86_64_STANDARD"
      instance_types = ["t3.micro"]

      min_size     = 3
      max_size     = 10
      desired_size = 3
    }
  }

  enable_cluster_creator_admin_permissions = true
}