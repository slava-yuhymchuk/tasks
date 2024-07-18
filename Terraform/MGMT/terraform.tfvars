# Management environment variables

# Global variables
profile = "slava"
region  = "il-central-1"
env     = "mgmt"

# VPC variables
vpc_name               = "vpc-mgmt"
cidr                   = "10.0.0.0/16"
azs                    = ["il-central-1a", "il-central-1b", "il-central-1c"]
private_subnets        = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
public_subnets         = ["10.0.10.0/24", "10.0.20.0/24", "10.0.30.0/24"]
enable_nat_gateway     = false
single_nat_gateway     = true
one_nat_gateway_per_az = false
enable_dns_hostnames   = true
enable_dns_support     = true
