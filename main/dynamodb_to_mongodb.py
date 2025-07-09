# main/dynamodb_to_mongodb.py
from extract.extract_from_dynamodb import extract_all_data
from transform.transform_projects import transform_projects
from load.load_to_mongodb import load_to_mongodb

if __name__ == "__main__":
    print(" Extracting from DynamoDB...")
    projects = extract_all_data()

    print(" Transforming data...")
    cleaned_projects = transform_projects(projects)

    print(" Loading to MongoDB...")
    load_to_mongodb(cleaned_projects)

    print(" ETL complete.")
