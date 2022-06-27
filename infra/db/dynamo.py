import pulumi_aws as aws

USERS_TABLE_NAME = "users-table"

users_table = aws.dynamodb.Table(
    USERS_TABLE_NAME,
    name=USERS_TABLE_NAME,
    attributes=[
        aws.dynamodb.TableAttributeArgs(
            name="id",
            type="S",
        )
    ],
    hash_key="id",
    read_capacity=1,
    write_capacity=1,
    stream_enabled=False,
)
