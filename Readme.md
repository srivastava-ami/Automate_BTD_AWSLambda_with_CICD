# Build & Deploy Template For AWS Lambda function
Building Lambda function and deploying it using the CI/CD pipeline to AWS

## Pre-requisites
* [github cli](https://cli.github.com/)
* Login to github cli using following commands

  ``` gh auth login ```
* Install the pre-requisites
  ```shell
  python3 -m pip install -r requirment.txt
  ```

## Important files
* ### env-secret
  * Put your AWS credential information
  ```
  AWS_ACCESS_KEY_ID=VALUE
  AWS_SECRET_ACCESS_KEY=VALUE
  AWS_REGION=VALUE
  AWS_STACK_NAME=VALUE
  AWS_S3_BUCKET=VALUE
  ```
* ### config.yml 
* It contains the parameter that are used in main script to deploy lambda and to create the repo and github
  * It looks like this 
  ```
  name: Internal-ami-action_workflow-test # name of the Stack to deploy
  runtime: python3.9
  repo-org: helpshift-solutions
  package-type: Zip
  repo-type: --private
  ```
## Create the lambda function that will deploy using CI/CD

  ```shell
  python3 main.py
  ```
Sample Output would look like following
```shell
$ python3 main.py                                                                                                                                       [3:05:36]
Please see the stack name will be: Internal-ami-action_workflow-test 
 For Customer/Internal: Internal 
 Domain: ami 
 Title: action_workflow-test

Based on your selections, the only Template available is Hello World Example.
We will proceed to selecting the Template as Hello World Example.

Based on your selections, the only dependency manager available is pip.
We will proceed copying the template using pip.

Cloning from https://github.com/aws/aws-sam-cli-app-templates (process may take a moment)

    -----------------------
    Generating application:
    -----------------------
    Name: Internal-ami-action_workflow-test
    Runtime: python3.9
    Architectures: x86_64
    Dependency Manager: pip
    Application Template: hello-world
    Output Directory: .
    
    Next steps can be found in the README file at ./Internal-ami-action_workflow-test/README.md
        

    Commands you can use next
    =========================
    [*] Create pipeline: cd Internal-ami-action_workflow-test && sam pipeline init --bootstrap
    [*] Validate SAM template: sam validate
    [*] Test Function in the Cloud: sam sync --stack-name {stack-name} --watch
    2022-09-11 03:06:21 Loading policies from IAM...                                                                                                          [3/4732]
    2022-09-11 03:06:31 Finished loading policies from IAM.                                                                                                           
    /Users/NAME/Downloads/Codebase/srivastava-ami-testrepo/Internal-ami-action_workflow-test/template.yaml is a valid SAM Template                          
    ../python_lambda_deploy_template.yml -> ./.github/workflows/python_lambda_deploy_template.yml                                                                     
    hint: Using 'master' as the name for the initial branch. This default branch name 
    hint: is subject to change. To configure the initial branch name to use in all
    hint: of your new repositories, which will suppress this warning, call:
    hint: 
    hint:   git config --global init.defaultBranch <name>
    hint: 
    hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
    hint: 'development'. The just-created branch can be renamed via this command:
    hint: 
    hint:   git branch -m <name>
    Initialized empty Git repository in /Users/NAME/Downloads/Codebase/srivastava-ami-testrepo/Internal-ami-action_workflow-test/.git/
    [master (root-commit) 35daf46] Template with default workflow
     15 files changed, 675 insertions(+)
     create mode 100644 .github/workflows/python_lambda_deploy_template.yml
     create mode 100644 .gitignore
     create mode 100644 README.md
     create mode 100644 __init__.py
     create mode 100644 events/event.json
     create mode 100644 hello_world/__init__.py
     create mode 100644 hello_world/app.py
     create mode 100644 hello_world/requirements.txt
     create mode 100644 template.yaml
     create mode 100644 tests/__init__.py
     create mode 100644 tests/integration/__init__.py
     create mode 100644 tests/integration/test_api_gateway.py
     create mode 100644 tests/requirements.txt
     create mode 100644 tests/unit/__init__.py
     create mode 100644 tests/unit/test_handler.py
    ✓ Created repository ORG/Internal-ami-action_workflow-test on GitHub
    ✓ Added remote git@github.com:helpshift-solutions/Internal-ami-action_workflow-test.git
    ✓ Pushed commits to git@github.com:ORG/Internal-ami-action_workflow-test.git
    ✓ Set Actions secret AWS_S3_BUCKET for ORG/Internal-ami-action_workflow-test
    ✓ Set Actions secret AWS_ACCESS_KEY_ID for ORG/Internal-ami-action_workflow-test
    ✓ Set Actions secret AWS_STACK_NAME for ORG/Internal-ami-action_workflow-test
    ✓ Set Actions secret AWS_REGION for ORG/Internal-ami-action_workflow-test
    ✓ Set Actions secret AWS_SECRET_ACCESS_KEY for ORG/Internal-ami-action_workflow-test
    Success

```