
# Configure AWS provider
provider "aws" {
  profile = var.profile
  region  = var.region
}

# Configure EKS module
module "eks" {
  
}
