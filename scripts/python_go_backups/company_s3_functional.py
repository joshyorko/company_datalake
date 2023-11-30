import csv
import io
from faker import Faker
from tqdm import tqdm
import time
import boto3

fake = Faker()

# Pure function to generate fake company
def generate_fake_company(fake, unique_names):
    attempts = 0
    while True:
        attempts += 1
        name = fake.company()
        if name not in unique_names:
            break
        if attempts >= 100:
            name += f"-{fake.random_int(min=1, max=9999)}"
            break
    unique_names.add(name)

    return {
        "name": name,
        "industry": fake.bs(),
        "employees": fake.random_int(min=1, max=10000),
        "revenue": fake.random_int(min=100000, max=1000000000),
        "location": fake.city()
    }

# Pure function to generate fake employee
def generate_fake_employee(fake, company):
    company_domain = company['name'].replace(' ', '').replace('.', '').replace(',', '').lower()
    first_name = fake.first_name()
    last_name = fake.last_name()
    return {
        "company_name": company['name'],
        "first_name": first_name,
        "last_name": last_name,
        "email": f"{first_name.lower()}.{last_name.lower()}@{company_domain}.com",
        "position": fake.job(),
        "salary": fake.random_int(min=40000, max=1500000)
    }

# Pure function to generate fake department
def generate_fake_department(fake, company):
    department_name = fake.job().split(" ")[0]
    return {
        "company_name": company['name'],
        "department_name": department_name,
        "manager_id": fake.random_int(min=1, max=999999),
        "budget": fake.random_int(min=10000, max=500000),
        "location": fake.city(),
        "start_date": fake.date_this_decade(),
        "end_date": fake.future_date(end_date="+5y"),
        "department_size": fake.random_int(min=10, max=100),
        "functional_area": fake.random_element(["R&D", "Sales", "Finance", "HR", "Operations"])
    }

# Function to write data to S3
def write_data_to_s3(data, s3_client, bucket_name, database_name, data_type):
    output = io.StringIO()
    csv_writer = csv.writer(output)
    csv_writer.writerow(data[0].keys())  # Header from dict keys

    for row in data:
        csv_writer.writerow(row.values())

    output.seek(0)
    key = f"{database_name}/{data_type}/data.csv"
    s3_client.put_object(Bucket=bucket_name, Key=key, Body=output.getvalue())
    output.close()

# Main script
if __name__ == "__main__":
    s3_client = boto3.client('s3')
    bucket_name = 'portfolio-company-datalake-jy'
    database_name = 'fake-companies'  # Replace with your actual database name

    # Create companies
    unique_names = set()
    companies = [generate_fake_company(fake, unique_names) for _ in tqdm(range(int(input('Enter Amount of Companies to Create: '))), desc="Creating companies")]

    # Create employees
    employees = [generate_fake_employee(fake, company) for company in tqdm(companies, desc="Creating employees") for _ in range(company['employees'])]

    # Create departments
    departments = [generate_fake_department(fake, company) for company in tqdm(companies, desc="Creating departments") for _ in range(fake.random_int(min=1, max=3))]

    # Write to S3
    write_data_to_s3(companies, s3_client, bucket_name, database_name, 'companies')
    write_data_to_s3(employees, s3_client, bucket_name, database_name, 'employees')
    write_data_to_s3(departments, s3_client, bucket_name, database_name, 'departments')
