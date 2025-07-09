# extract/extract_from_dynamodb.py
from config.aws_config import get_dynamodb_resource

def extract_all_data():
    dynamodb = get_dynamodb_resource()
    table = dynamodb.Table("ProjectData")
    response = table.scan()
    data = response["Items"]

    while "LastEvaluatedKey" in response:
        response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
        data.extend(response["Items"])

    return data
