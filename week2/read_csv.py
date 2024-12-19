import csv
import re
import boto3
import certifi
from botocore.exceptions import NoCredentialsError
from botocore.config import Config

# Create a DynamoDB client with certifi's CA bundle
client = boto3.client(
    'dynamodb',
    region_name='us-east-1',
)

def read_csv(file_name):
    data = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert company_zip and contact_mailing_zip to integers
            if 'company_zip' in row:
                row['company_zip'] = int(row['company_zip'])
            if 'contact_mailing_zip' in row:
                row['contact_mailing_zip'] = int(row['contact_mailing_zip'])
            data.append(row)
    return data

company_data = read_csv('company.csv')
for i in range(len(company_data)):
	for key in company_data[i]:
		company_data[i][key]={
			"S":str(company_data[i][key])
		}

contact_data = read_csv('contact.csv')

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

for contact in contact_data:
    if not validate_email(contact["contact_email"]):
        print(f"Invalid email for {contact['first_name']} {contact['last_name']}: {contact['contact_email']}")
    else:
        print(f"{contact['contact_email']} is verified")

for i in range(len(contact_data)):
	for key in contact_data[i]:
		contact_data[i][key]={
			"S":str(contact_data[i][key])
		}
print(company_data,contact_data)

def put_item_to_dynamodb(data, table_name):
    try:
        #table = dynamodb.Table(table_name)
        for item in data:
            #response = table.put_item(Item=item)
            response = client.put_item(Item=item, ReturnConsumedCapacity='TOTAL',TableName=table_name)
            print(f"Item inserted: {response}")
    except NoCredentialsError:
        print("Credentials not available")

put_item_to_dynamodb(company_data, 'CompanyTable')  
put_item_to_dynamodb(contact_data, 'ContactTable')  

print(company_data)  
print(contact_data)  
