import json
import yaml
import pulumi_aws as aws


swagger_dict = yaml.safe_load(open("./api/openapi.yml").read())


def get_apigateway_integration(lambda_uri):
    return {
        "uri": lambda_uri,
        "passthroughBehavior": "when_no_match",
        "httpMethod": "POST",
        "type": "aws_proxy",
    }


def create_api_permission(lambda_name):
    aws.lambda_.Permission(
        f"{lambda_name}-permission",
        action="lambda:InvokeFunction",
        function=lambda_name,
        principal="apigateway.amazonaws.com",
        source_arn=api.execution_arn.apply(lambda arn: f"{arn}/*/*/*"),
    )


lambda_get_users = aws.lambda_.get_function("lambda_get_users")
lambda_create_user = aws.lambda_.get_function("lambda_create_user")
lambda_get_user = aws.lambda_.get_function("lambda_get_user")
lambda_delete_user = aws.lambda_.get_function("lambda_delete_user")


swagger_dict["paths"]["/users"]["get"][
    "x-amazon-apigateway-integration"
] = get_apigateway_integration(lambda_get_users.invoke_arn)

swagger_dict["paths"]["/users"]["post"][
    "x-amazon-apigateway-integration"
] = get_apigateway_integration(lambda_create_user.invoke_arn)

swagger_dict["paths"]["/users/{user_id}"]["get"][
    "x-amazon-apigateway-integration"
] = get_apigateway_integration(lambda_get_user.invoke_arn)

swagger_dict["paths"]["/users/{user_id}"]["delete"][
    "x-amazon-apigateway-integration"
] = get_apigateway_integration(lambda_delete_user.invoke_arn)


api = aws.apigateway.RestApi(
    "test-api",
    name="test-api",
    policy=json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "execute-api:Invoke",
                    "Resource": ["*"],
                }
            ],
        }
    ),
    endpoint_configuration={"types": "PRIVATE"},
    body=json.dumps(swagger_dict),
)

create_api_permission(lambda_get_users.function_name)
create_api_permission(lambda_create_user.function_name)
create_api_permission(lambda_get_user.function_name)
create_api_permission(lambda_delete_user.function_name)
