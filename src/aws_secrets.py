# Unmodified aws demo function to get secrets
# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "prod/scrapping/venvv"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    return secret

if __name__ == "__main__":
    import json


    secrets = get_secret()
    secret_dic = json.loads(secrets)
    print(secret_dic["SFUSER"])
    print(secret_dic["SFACCOUNT"])
    print(secret_dic["SFWAREHOUSE"])
    print(secret_dic["SFDATABASE"])
    print(secret_dic["SFSCHEMA"])
    print(secret_dic["SFROLE"])