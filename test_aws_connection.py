import boto3

def test_connection():
    try:
        dynamodb = boto3.client('dynamodb', region_name='us-east-1')
        response = dynamodb.list_tables()
        print("DynamoDB connection successful.")
        print("Available Tables:", response.get('TableNames', []))
    except Exception as e:
        print("AWS connection failed.")
        print("Error:", str(e))

if __name__ == "__main__":
    test_connection()
