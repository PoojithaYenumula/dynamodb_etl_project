# load/load_to_dynamodb.py

import boto3
import json
import os

def load_from_file_and_insert():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table("ProjectData")

    with open("data/project.txt", "r") as f:
        raw_data = f.read()

    # Split by newlines or parse multiple JSON blocks
    records = [json.loads(block) for block in raw_data.strip().split('\n') if block.strip()]

    for item in records:
        # Ensure technologies is stored as a list
        if isinstance(item.get("technologies"), str):
            item["technologies"] = [tech.strip() for tech in item["technologies"].split(',')]
        table.put_item(Item=item)

    print(f" {len(records)} records loaded into DynamoDB.")

if __name__ == "__main__":
    load_from_file_and_insert()
