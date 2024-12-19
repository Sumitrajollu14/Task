import csv
import json

def create_csv_files():
    company_data = [
        {"company_id": 13206991, "company_name": "Accenture", "company_address": "Gachibowli", "company_country": "India", 
         "company_city": "Hyderabad", "company_zip": 500075, "company_code": "ACN001", "company_state": "Telangana", "company_phone_number": "12345677890", "company_region_code": "US"},
        {"company_id": 13206662, "company_name": "Google", "company_address": "HiTechcity", "company_country": "India", 
         "company_city": "Telangana", "company_zip": 500085, "company_code": "CG002", "company_state": "Telangana", "company_phone_number": "9876543210", "company_region_code": "UK"}
    ]

    contact_data = [
        {"contact_id": 901234, "contact_company_id": 1234, "first_name": "Sumitra", "last_name": "Jollu", 
         "contact_email": "sumitra.jollu@example.com", "contact_phone": "9876543210", "contact_mailing_address": "123 Street", 
         "contact_mailing_city": "Hyderabad", "contact_mailing_state": "Telangana", "contact_mailing_zip": 10001, "contact_mailing_country": "US"},
        {"contact_id": 345678, "contact_company_id": 5678, "first_name": "Accenture", "last_name": "Solutions", 
         "contact_email": "accenture.solutions@example.com", "contact_phone": "1234567890", "contact_mailing_address": "456 Another St", 
         "contact_mailing_city": "London", "contact_mailing_state": "England", "contact_mailing_zip": 20002, "contact_mailing_country": "UK"}
    ]

    # Writing company data to company.csv
    with open('company.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["company_id", "company_name", "company_address", "company_country", 
                                                  "company_city", "company_zip", "company_code", "company_state", 
                                                  "company_phone_number", "company_region_code"])
        writer.writeheader()
        writer.writerows(company_data)

    # Writing contact data to contact.csv
    with open('contact.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["contact_id", "contact_company_id", "first_name", "last_name", "contact_email", 
                                                  "contact_phone", "contact_mailing_address", "contact_mailing_city", 
                                                  "contact_mailing_state", "contact_mailing_zip", "contact_mailing_country"])
        writer.writeheader()
        writer.writerows(contact_data)

    print("CSV files created successfully!")
    
# Define a function to load the configuration from a JSON file
def load_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)

# Load the configuration from the company_config.json file
config = load_config('company_config.json')
print(config)

# Function to validate if the company_code exists in the company_code_picklist
def validate_company_code(company_code, config):
    if company_code in config['company_code_picklist']:
        print(f"Company code {company_code} is valid.")
    else:
        print(f"Company code {company_code} is not valid.")

company_code = "ACN001"
validate_company_code(company_code, config)

create_csv_files()
