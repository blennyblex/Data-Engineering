variable "credentials" {
  description = "My Credentials"
  default     = "/home/blessing/Data-Engineering/keys/my_cred.json"
}

variable "project" {
  description = "Project"
  default     = "learned-maker-461014-p6"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}


variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My Bigquery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "learned-maker-461014-p6-terra-bucket"
}

variable "gcs_bucket_class" {
  description = "My Storage Bucket Class"
  default     = "STANDARD"
}