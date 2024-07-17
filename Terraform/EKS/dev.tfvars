# Development environment variables

profile                        = "slava"
region                         = "il-central-1"
env                            = "dev"
cluster_name                   = "eks-dev"
cluster_version                = "1.30"
cluster_endpoint_public_access = true
vpc_id                         = "vpc-0563fd6d7988182ad"
subnet_ids                     = ["subnet-0cc7f69f715580999", "subnet-0f133e7a274276ec8", "subnet-050bbdc261557f780"]
instance_types                 = ["t3.small"]
capacity_type                  = "SPOT"
ami_type                       = "AL2023_x86_64_STANDARD"
min_size                       = 2
max_size                       = 10
desired_size                   = 2

# aws eks update-kubeconfig --name eks-dev --region il-central-1