# Production environment variables

profile                        = "slava"
region                         = "il-central-1"
env                            = "prod"
cluster_name                   = "eks-prod"
cluster_version                = "1.30"
cluster_endpoint_public_access = true
vpc_id                         = "vpc-09cbc6fbeb22cdcbc"
subnet_ids                     = ["subnet-0011daa0e00b43349", "subnet-0efc8ad71eb883a68", "subnet-0b1cf15afd537dc48"]
instance_types                 = ["t3.micro"]
ami_type                       = "AL2023_x86_64_STANDARD"
min_size                       = 6
max_size                       = 10
desired_size                   = 6

# aws eks update-kubeconfig --name eks-prod --region il-central-1