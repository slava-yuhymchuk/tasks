# Configure EKS module
module "eks" {
  source = "terraform-aws-modules/eks/aws"

  cluster_name    = "eks-${var.env}"
  cluster_version = var.cluster_version

  cluster_endpoint_public_access = var.cluster_endpoint_public_access

  cluster_addons = {
    coredns = {}
    eks-pod-identity-agent = {}
    kube-proxy = {}
    vpc-cni    = {}
  }

  # vpc_id     = var.vpc_id
  vpc_id     = module.vpc.vpc_id 
  # subnet_ids = var.subnet_ids
  subnet_ids = module.vpc.private_subnets

  eks_managed_node_group_defaults = {
    instance_types = var.instance_types
    capacity_type  = var.capacity_type
  }

  eks_managed_node_groups = {
    (var.cluster_name) = {
      ami_type       = var.ami_type
      instance_types = var.instance_types
      capacity_type  = var.capacity_type

      min_size     = var.min_size
      max_size     = var.max_size
      desired_size = var.desired_size
    }
  }

  enable_cluster_creator_admin_permissions = true
}

resource "aws_security_group_rule" "sealed-secrets-access" {
  type                     = "ingress"
  from_port                = 8080
  to_port                  = 8080
  protocol                 = "tcp"
  security_group_id        = module.eks.node_security_group_id
  source_security_group_id = module.eks.cluster_security_group_id
  description              = "Allow inbound traffic to sealed-secrets controller"
}
