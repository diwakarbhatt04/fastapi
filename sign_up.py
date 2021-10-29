import os
import boto3
from dotenv import load_dotenv
load_dotenv()

username = 'test_user@gmail.com'
password = 'Diwakar@123'

# client = boto3.client('cognito-idp', region_name=os.getenv('COGNITO_REGION_NAME'))
# response = client.sign_up(
#     ClientId=os.getenv('COGNITO_USER_CLIENT_ID'),
#     Username=username,
#     Password=password
# )

client = boto3.client('cognito-idp', region_name='us-east-2')
response = client.sign_up(
    ClientId='7fi919di1fvgpbr6uo8bhtmdg9',
    Username=username,
    Password=password
)


print(response)