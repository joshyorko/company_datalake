

class SoftwareCompany:
    def __init__(self, name=None, industry=None, employees=None, revenue=None, location=None):
        self.name = name
        self.industry = industry
        self.employees = employees
        self.revenue = revenue
        self.location = location

    def get_fake_company(self, fake, unique_names):
        attempts = 0
        while True:
            attempts += 1
            self.name = fake.company()
            if self.name not in unique_names:
                break
            if attempts >= 100:
                self.name += f"-{fake.random_int(min=1, max=9999)}"
                break
        unique_names.add(self.name)
        
        self.industry = fake.bs()
        self.employees = fake.random_int(min=1, max=10000)
        self.revenue = fake.random_int(min=100000, max=1000000000)
        self.location = fake.city()
        return self

class Employee:
    def __init__(self, company_name):
        self.company_name = company_name
        self.first_name = None
        self.last_name = None
        self.email = None
        self.position = None
        self.salary = None

    def get_fake_employee(self, fake, company_domain):
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@{company_domain}.com"
        self.position = fake.job()
        self.salary = fake.random_int(min=40000, max=1500000)
        return self
class Department:
    def __init__(self, company_name):
        self.company_name = company_name
        self.department_name = None
        self.manager_id = None  # Assume an employee ID will be the manager's ID
        self.budget = None
        self.location = None
        self.start_date = None
        self.end_date = None
        self.department_size = None
        self.functional_area = None

    def get_fake_department(self, fake):
        self.department_name = fake.job().split(" ")[0]  # Generating fake department names
        self.manager_id = fake.random_int(min=1, max=999999)
        self.budget = fake.random_int(min=10000, max=500000)
        self.location = fake.city()
        self.start_date = fake.date_this_decade()
        self.end_date = fake.future_date(end_date="+5y")
        self.department_size = fake.random_int(min=10, max=100)
        self.functional_area = fake.random_element(["R&D", "Sales", "Finance", "HR", "Operations"])
        return self