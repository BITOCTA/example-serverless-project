import json
import os

import pulumi
import pulumi_aws as aws
from db.dynamo import USERS_TABLE_NAME

API_LAMBDAS_PATH = "../backend/api"

REGION = aws.get_region().name
ACCOUNT = aws.get_caller_identity().account_id

for lambda_dir in os.listdir(API_LAMBDAS_PATH):

    lambda_role = aws.iam.Role(
        f"{lambda_dir}-iam-role",
        assume_role_policy="""{
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
            }
        ]
    } """,
    )

    aws.iam.RolePolicy(
        f"{lambda_dir}-iam-role-policy",
        role=lambda_role.id,
        policy=json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": "logs:CreateLogGroup",
                        "Resource": f"arn:aws:logs:{REGION}:{ACCOUNT}:*",
                    },
                    {
                        "Effect": "Allow",
                        "Action": ["logs:CreateLogStream", "logs:PutLogEvents"],
                        "Resource": [
                            f"arn:aws:logs:{REGION}:{ACCOUNT}:log-group:/aws/lambda/*:*"
                        ],
                    },
                    {
                        "Action": [
                            "dynamodb:*",
                        ],
                        "Resource": "*",
                        "Effect": "Allow",
                    },
                ],
            }
        ),
    )

    aws.lambda_.Function(
        lambda_dir,
        name=lambda_dir,
        code=pulumi.asset.FileArchive(os.path.join(API_LAMBDAS_PATH, lambda_dir)),
        role=lambda_role.arn,
        handler="app.lambda_handler",
        runtime="python3.8",
        environment={
            "variables": {
                "PYTHONPATH": "/var/task/lib",
                "USERS_TABLE_NAME": USERS_TABLE_NAME,
            }
        },
    )
