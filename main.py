#!/usr/local/bin/python3.9
import os
import yaml

# Reading the config file and storing the data in the dictionary
with open("config.yml", 'r') as f:
    config = yaml.safe_load(f)


# Verify nomenclature to make sure lambda stack name must be like CUSTOMER-DOMAIN-PROJECTNAME
def verifyNomenclature():
    stack = config['name'].split('-')
    if len(stack) <= 3:
        print("Should be in format customer/team-domain-toolname")
        verified = False
    else:
        verified = True
        print(f"Please see the stack name will be: {config['name']} "
              f"\n For Customer/Internal: {stack[0]} "
              f"\n Domain: {stack[1]} "
              f"\n Title: {'-'.join(stack[2:])}")

    return verified


# Creating the template lamda function using "hello-world" app template
def create_sam_template():
    param = "sam init "\
            f"-r {config['runtime']} "\
            f"-p {config['package-type']} "\
            f"-n {config['name']} "\
            "--no-tracing "\
            "--app-template 'hello-world' "
    sam = os.system(param)
    return sam


# Validating is the SAM template is created successfully.
def vaidate_sam_template():
    param = f"sam validate -t {config['name']}/template.yaml"
    return os.system(param)


# Creting the local directory with all the workflow and then converting it into
# github repo and pushing the initial commits to the repo
def create_gitrepo_with_action_workflow():
    cd = f"cd {config['name']}"
    copy_workflow_file = f"mkdir -p .github/workflows && cp -vf ../python_lambda_deploy_template.yml " \
                         f"./.github/workflows/ "
    create_repo = f"gh repo create {config['repo-org']}/{config['name']} {config['repo-type']} " \
                  f"--source=. --remote=upstream --push"
    set_repo_secrets = f"gh secret set -f ../env-secret"
    first_commit = f"git init && git add -A && git commit -m 'Template with default workflow' "
    os.system(f"{cd} && {copy_workflow_file} && {first_commit} && {create_repo} && {set_repo_secrets} ")


# Call the main function and running only when the nomenclature is followed.
if __name__ == "__main__":
    if verifyNomenclature():
        create_sam_template()
        vaidate_sam_template()
        create_gitrepo_with_action_workflow()
        print("Success")
    else:
        print("Failed to create the sample")