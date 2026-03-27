# -*- coding: utf-8 -*-

"""
Infrastructure Terraform Project README
=====================================

This project provides a Terraform configuration for managing infrastructure
resources on AWS.

Setup
-----

1. Clone the repository: `git clone https://github.com/your-username/infra-terraform.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Initialize the Terraform working directory: `terraform init`
4. Verify the infrastructure configuration: `terraform plan`

Usage
-----

1. Create a new AWS account or use an existing one.
2. Configure the AWS provider: `terraform apply`
3. Provision the infrastructure resources: `terraform apply`

Troubleshooting
--------------

* Check the Terraform logs for errors: `terraform console`
* Verify the AWS account credentials: `aws sts get-caller-identity`
* Consult the Terraform documentation: <https://www.terraform.io/docs>

License
-------

This project is licensed under the MIT License.
"""

import os

def main():
    # Check if the user is running the script from the project root directory
    if os.getcwd() != os.path.dirname(os.path.abspath(__file__)):
        print("Error: Please run the script from the project root directory.")
        return 1

    # Check if the required dependencies are installed
    if not os.path.exists('requirements.txt'):
        print("Error: Please install the required dependencies by running 'pip install -r requirements.txt'.")
        return 1

    # Initialize the Terraform working directory
    if not os.path.exists('.terraform'):
        os.mkdir('.terraform')
        os.symlink('terraform.rc', '.terraform/terraform.rc')

    # Verify the infrastructure configuration
    os.system('terraform init')
    os.system('terraform console')

    # Provision the infrastructure resources
    os.system('terraform apply')

if __name__ == '__main__':
    main()