terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.37.0"
    }
  }
}

provider "google" {
  # Configuration options
#   credentials = "./keys/my_cred.json"
  project = "learned-maker-461014-p6"
  region  = "us-central1"
}


resource "google_storage_bucket" "demo-bucket" {
  name          = "learned-maker-461014-p6-terra-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}