# example-serverless-project

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
