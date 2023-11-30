from faker import Faker
import csv
from tqdm import tqdm
import time


# data generation functions
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

def generate_fake_employee(fake, company_name, company_domain):
    first_name = fake.first_name()
    last_name = fake.last_name()
    return {
        "company_name": company_name,
        "first_name": first_name,
        "last_name": last_name,
        "email": f"{first_name.lower()}.{last_name.lower()}@{company_domain}.com",
        "position": fake.job(),
        "salary": fake.random_int(min=40000, max=1500000)
    }

def generate_fake_department(fake, company_name):
    department_name = fake.job().split(" ")[0]
    return {
        "company_name": company_name,
        "department_name": department_name,
        "manager_id": fake.random_int(min=1, max=999999),
        "budget": fake.random_int(min=10000, max=500000),
        "location": fake.city(),
        "start_date": fake.date_this_decade(),
        "end_date": fake.future_date(end_date="+5y"),
        "department_size": fake.random_int(min=10, max=100),
        "functional_area": fake.random_element(["R&D", "Sales", "Finance", "HR", "Operations"])
    }

# data writing functions
def create_and_write_entities(entity_generator, entity_count, csv_writer, **kwargs):
    for _ in tqdm(range(entity_count), desc=f"Creating {entity_generator.__name__}"):
        entity = entity_generator(**kwargs)
        csv_writer.writerow(entity.values())

if __name__ == "__main__":
    fake = Faker()
    unique_names = set()

    # Create and write companies
    with open("companies.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Name", "Industry", "Employees", "Revenue", "Location"])
        company_count = int(input('Enter Amount of Companies to Create: '))
        create_and_write_entities(generate_fake_company, company_count, csv_writer, fake=fake, unique_names=unique_names)

    # Create and write employees and departments
    for company in unique_names:
        company_domain = company.replace(' ', '').replace('.', '').replace(',', '').lower()

        with open(f"{company}_employees.csv", "w", newline="") as csvfile:
            employee_csv_writer = csv.writer(csvfile)
            employee_csv_writer.writerow(["Company_Name", "First_Name", "Last_Name", "Email", "Position", "Salary"])
            create_and_write_entities(generate_fake_employee, 10, employee_csv_writer, fake=fake, company_name=company, company_domain=company_domain)

        with open(f"{company}_departments.csv", "w", newline="") as csvfile:
            department_csv_writer = csv.writer(csvfile)
            department_csv_writer.writerow(["Company_Name", "Department_Name", "Manager_ID", "Budget", "Location", "Start_Date", "End_Date", "Department_Size", "Functional_Area"])
            create_and_write_entities(generate_fake_department, 3, department_csv_writer, fake=fake, company_name=company)

