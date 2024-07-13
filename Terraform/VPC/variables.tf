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

variable "vpc_name" {
  description = "VPC name"
  type        = string
  default     = "vpc-dev"
}

variable "cidr" {
  description = "VPC CIDR block"
  type        = string
  default     = "10.0.0.0/16"
}

variable "azs" {
  description = "Availability Zones"
  type        = list(string)
  default     = ["il-central-1a", "il-central-1b", "il-central-1c"]
}

variable "private_subnets" {
  description = "Private subnets"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

variable "public_subnets" {
  description = "Public subnets"
  type        = list(string)
  default     = ["10.0.10.0/24", "10.0.20.0/24", "10.0.30.0/24"]
}

variable "enable_nat_gateway" {
  description = "Create NAT gateway for private networks"
  type        = bool
  default     = true
}

variable "single_nat_gateway" {
  description = "Create single NAT gateway shared across all private networks"
  type        = bool
  default     = true
}

variable "one_nat_gateway_per_az" {
  description = "Create one NAT gateway per availability zone"
  type        = bool
  default     = false
}