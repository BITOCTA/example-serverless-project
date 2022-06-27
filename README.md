# example-serverless-project

## Overview

Sample serverless (using only serverless AWS services) project with simple users CRUD inside. Code is written in pure Python, while all of the insfrastructure is defined using Pulumi IaC tool.

Project architecture is described on the diagram below:

![project architecture](https://user-images.githubusercontent.com/33602278/175916423-ef079f09-ec8e-4006-94f8-c7196ba08251.png)

## Build

Go to backend/ folder and build using tasks.sh script.

```bash
cd backend
./tasks.sh build
```

If build is successful, you should have lib/ folder in every lambda folder in backend/api.

## Deploy

### Prerequisites

[Pulumi](https://www.pulumi.com/docs/get-started/install/) installed. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed and configured. AWS profile configured.

### How to

Login using pulumi (e.g to AWS S3 bucket).

```bash
pulumi login s3://
```

Go to the infra/ folder and create a new Pulumi stack.

```bash
cd infra
pulumi stack select dev --create
```

Deploy using Pulumi

```
pulumi up
```
