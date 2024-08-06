# Development environment variables

# Global variables
profile = "slava"
region  = "il-central-1"
env     = "dev"

# VPC variables
vpc_name               = "vpc-dev"
cidr                   = "10.0.0.0/16"
azs                    = ["il-central-1a", "il-central-1b", "il-central-1c"]
private_subnets        = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
public_subnets         = ["10.0.10.0/24", "10.0.20.0/24", "10.0.30.0/24"]
enable_nat_gateway     = true
single_nat_gateway     = true
one_nat_gateway_per_az = false
enable_dns_hostnames   = true
enable_dns_support     = true

# EKS variables
cluster_name                   = "eks-dev"
cluster_version                = "1.30"
cluster_endpoint_public_access = true
# vpc_id                         = "vpc-0563fd6d7988182ad"
# subnet_ids                     = ["subnet-0cc7f69f715580999", "subnet-0f133e7a274276ec8", "subnet-050bbdc261557f780"]
instance_types                 = ["t3.small"]
capacity_type                  = "SPOT"
ami_type                       = "AL2023_x86_64_STANDARD"
min_size                       = 2
max_size                       = 4
desired_size                   = 2
