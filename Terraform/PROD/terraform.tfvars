# Production environment variables

# Global variables
profile = "slava"
region  = "il-central-1"
env     = "prod"

# VPC variables
vpc_name               = "vpc-prod"
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
cluster_name                   = "eks-prod"
cluster_version                = "1.29"
cluster_endpoint_public_access = true
# vpc_id                         = "vpc-09cbc6fbeb22cdcbc"
# subnet_ids                     = ["subnet-0011daa0e00b43349", "subnet-0efc8ad71eb883a68", "subnet-0b1cf15afd537dc48"]
instance_types                 = ["t3.small"]
capacity_type                  = "ON_DEMAND"
ami_type                       = "AL2023_x86_64_STANDARD"
min_size                       = 2
max_size                       = 10
desired_size                   = 2
