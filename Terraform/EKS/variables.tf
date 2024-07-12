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
