terraform {
  backend "gcs" {
    bucket = "qwiklabs-gcp-02-9e29b78d2367-terraform-state"
    prefix = "agentic-era-hack/prod"
  }
}
