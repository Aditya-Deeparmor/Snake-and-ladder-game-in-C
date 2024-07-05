provider "aws" {
  region = "us-west-2"
}

resource "aws_secretsmanager_secret" "example" {
  name        = "example-password"
  description = "This is a sample password stored in AWS Secrets Manager"
}

resource "aws_secretsmanager_secret_version" "example" {
  secret_id     = aws_secretsmanager_secret.example.id
  secret_string = jsonencode({
    password = "ExamplePassword123!"
  })
}

output "secret_arn" {
  value = aws_secretsmanager_secret.example.arn
}

output "secret_id" {
  value = aws_secretsmanager_secret.example.id
}
